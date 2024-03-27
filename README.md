# Aadhar-IFSC-Verification
Verify Aadhar and IFSC Code through Selenium & python
# Modules
```bash
pip install selenium
```
# Methods
create automation bot
```python
bot = WebAutomation()
bot = WebAutomation(console=True)                       # for headless automation withoutb opening the browser window
```
Verify Aadhar
```python
uidai_bot = AadharVerification(bot.start())
html_captcha = uidai_bot.getCaptcha()['captcha']        # generate HTML code for Captcha 
uidai_bot.inputDetails(<aadhar_number>,<captcha>)       # Enter Aadhar Number, Captcha Code respectively
uidai_bot.submit()                                      # Submit for verification
uidai_bot.fetchResponse()                               # Fetch the response
```
Verify IFSC Code
```python
IFSC_Verification = IFSC_Verification(bot.start())
IFSC_Verification.inputDetails(<IFSC_Code>)            # Enter IFSC Code for verification
IFSC_Verification.submit()                             # Submit for verification
IFSC_Verification.fetchResponse()                      # Fetch response
```
## Important
- every steps returns the status and response in the dict datatype.
- replace the variables `<aadhar_number>`, `<captcha>`, `<IFSC_Code>`.
- this is *not fully developed to handle the errors* in the verification.
- `html_captcha = uidai_bot.getCaptcha()['captcha']` returns the *HTML code for the captcha*, useful in case of [*headless automation*](#methods).

## for more detail and information about its working
- [Aadhar Verification](https://myaadhaar.uidai.gov.in/check-aadhaar-validity)
- [IFSC Verification](https://ifsc.bankifsccode.com/)
