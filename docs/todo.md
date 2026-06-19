# [TODO] X-Bot Task Checklist

## GreenHaven (GH) - [STATUS] Blocked (Suspended)
- [ ] [ERR] One or more client apps suspended. [FIX] Delete suspended app in X Developer Portal first.
- [ ] GreenHaven: Create a new App in the X Developer Portal
- [ ] GreenHaven: Configure App Permissions to 'Read and Write'
- [ ] GreenHaven: Generate new Consumer Keys and Access Tokens
- [ ] GreenHaven: Update config/credentials.env with new GH_ keys
- [ ] GreenHaven: Run upload_secrets.ps1 to upload keys to GitHub

## Moonchill (MC) - [STATUS] Done
- [x] Moonchill: Verify and generate unique keys in the X Developer Portal
- [x] Moonchill: Update config/credentials.env with new MC_ keys
- [x] Moonchill: Run upload_secrets.ps1 to upload keys to GitHub

## Stray Cat 1 (SC1) - [STATUS] Action Required (402 Payment Required)
- [x] [ERR] HTTPException 402 Payment Required. [FIX] Purchase API credits on X Developer Console.
- [x] Stray Cat 1: Add keys to config/credentials.env under SC1_ keys
- [x] Stray Cat 1: Run upload_secrets.ps1 to upload keys to GitHub

## Stray Cat 2 (SC2) - [STATUS] Action Required (402 Payment Required)
- [ ] [ERR] HTTPException 402 Payment Required. [FIX] Purchase API credits on X Developer Console.
- [x] Stray Cat 2: Verify App permissions are set to 'Read and Write'
- [x] Stray Cat 2: Regenerate keys/tokens in X Developer Portal to resolve 401
- [x] Stray Cat 2: Add keys to config/credentials.env under SC2_ keys
- [x] Stray Cat 2: Run upload_secrets.ps1 to upload keys to GitHub