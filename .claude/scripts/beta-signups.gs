/**
 * idiosync — beta signups.
 *
 * This is NOT part of the site. It lives in Google Apps Script, bound to
 * the signup spreadsheet, and the site's beta box POSTs to its deployed
 * URL. The copy here is the source of record, because the copy in Google
 * is in a window nobody will think to look in.
 *
 * To set it up:
 *   1. Make a Google Sheet. Name the first tab `signups` exactly.
 *   2. Put three headers in row 1: Email, Signed up, Source.
 *   3. Extensions -> Apps Script. Delete what's there, paste this in, Save.
 *   4. Deploy -> New deployment -> type "Web app".
 *        Execute as:    Me
 *        Who has access: Anyone            <- not "Anyone with Google account"
 *      Deploy, approve the scary-looking permission screen, copy the
 *      /exec URL.
 *   5. Paste that URL into BETA_ENDPOINT in index.html.
 *
 * Changing this file does nothing until you paste it into Apps Script and
 * run Deploy -> Manage deployments -> Edit -> New version. A plain Save
 * does NOT update what the deployed URL serves. That is the single most
 * common way this appears broken when it isn't.
 *
 * The /exec URL is public by necessity -- a static page has no way to hold
 * a secret -- so anyone who finds it can post to it. That is why there is
 * a honeypot on the form, a shape check here, and a dedupe: the realistic
 * failure is drive-by bot spam filling the sheet, not anything dangerous.
 * If it does get hit, the fix is Deploy -> Archive and a fresh URL.
 */

var SHEET_NAME = 'signups';

function doPost(e) {
  var result = { ok: false };

  /* Two posts landing at once would otherwise read the same last row and
     one would overwrite the other. Thirty seconds is far longer than this
     ever needs; it is a ceiling, not a wait. */
  var lock = LockService.getScriptLock();
  try {
    lock.waitLock(30000);

    var data = JSON.parse(e.postData.contents);
    var email = String(data.email || '').trim();

    /* Same loose shape test as the page. Deliberately not a rulebook --
       anything stricter rejects real addresses. The page checks too; this
       is here because the page's check is not a security boundary, it is
       a courtesy to whoever typed the address. */
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) {
      throw new Error('not an address');
    }

    var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEET_NAME);
    if (!sheet) throw new Error('no tab named ' + SHEET_NAME);

    /* Dedupe, case-insensitively. Someone signing up twice is far more
       likely to be the same person double-tapping than two people, and a
       list with duplicates in it is a list you have to clean before you
       can use it. */
    var lastRow = sheet.getLastRow();
    var seen = [];
    if (lastRow > 1) {
      seen = sheet.getRange(2, 1, lastRow - 1, 1).getValues().map(function (row) {
        return String(row[0]).trim().toLowerCase();
      });
    }

    if (seen.indexOf(email.toLowerCase()) === -1) {
      sheet.appendRow([email, new Date(), String(data.source || '')]);
    }

    /* Either way the answer is yes. Telling someone "you already signed
       up" is a correction nobody asked for. */
    result.ok = true;

  } catch (err) {
    result.error = String(err && err.message ? err.message : err);
  } finally {
    try { lock.releaseLock(); } catch (ignored) {}
  }

  return ContentService
    .createTextOutput(JSON.stringify(result))
    .setMimeType(ContentService.MimeType.JSON);
}

/**
 * Deployed web apps answer GET as well, and a browser pointed at the /exec
 * URL will send one. Answering plainly makes "is it deployed?" something
 * you can check by opening the URL, rather than by submitting the form and
 * guessing.
 */
function doGet() {
  return ContentService
    .createTextOutput(JSON.stringify({ ok: true, note: 'idiosync beta endpoint' }))
    .setMimeType(ContentService.MimeType.JSON);
}

/**
 * Run this from the Apps Script editor to check the sheet end of things
 * without involving the site. It appends a test row; delete it after.
 */
function selfTest() {
  var out = doPost({ postData: { contents: JSON.stringify({
    email: 'test@example.com',
    source: 'selfTest'
  }) } });
  Logger.log(out.getContent());
}
