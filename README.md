## **Krombopulos Michael (KMike)**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;KMike is a ransomware that I decided to create for learning about the inner workings of ransomware.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;It is written in Python, contrary to C or C++ which are supposed to be the languages for malware programming.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python was chosen because it was too much of a hassle to set up the C development environment in my Macbook and I have no intention of deploying the malware, so the performance and size do not matter. The ransomware design intentionally includes some choices to deter people from using it for nefarious purposes.    


## **Getting Started**
Instructions on how to go about setting up in your local machine  

### Prerequistes
To be filled

### Installing/Building
To be filled


## **Feature List:**
 * Basic Funcionality
    * ~~Encrypt, Decrypt Files~~  
    * ~~Delete Original Files~~
    * ~~Generate Random Bitcoin Address~~
    * ~~Show ransom message~~
    * Make the python code into an executable
    * ~~Use a domain generation algorithm~~
    * Priviledge checking     
    * Delete Shadow files
 * Write a C&C server
    * ~~Auto Payment Verification~~
 * Evasion Techniques
    * Sandbox Evasion  
    * AV Evasion  
    * Obfuscate Code
 * Nice-to-have Features
    * The ransom note and the process should persist across restarts  
    * Multithreading/multiprocessing to speed up encryption
    * ~~Collect statistics about the user~~
    * ~~[`Get C&C server via unusual mechanism`](https://www.zdnet.com/article/astaroth-malware-hides-command-servers-in-youtube-channel-descriptions/)~~
    * [`Shutdown some processes before encrypting files to ensure no write lock is present`](https://securityaffairs.co/wordpress/103030/malware/sodinokibi-ransomware-new-feature.html)  
 


## **License**
    The project is distributed under GNU GPL 3.0
      

## **Mentions**
 * [The post that started this all - DespaREto](https://medium.com/@despaREto/how-not-to-write-ransomware-1985aa1384a3)
 * [Encryption Scheme - Tarcísio Marinho](https://medium.com/@tarcisioma/ransomware-encryption-techniques-696531d07bb9)     
 * [Generating Bitcoin Wallet Address - Timur Badretdinov](https://www.freecodecamp.org/news/how-to-create-a-bitcoin-wallet-address-from-a-private-key-eca3ddd9c05f/)   
