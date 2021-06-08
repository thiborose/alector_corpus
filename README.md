# alector_corpus

⚠️    I do not own this corpus   ⚠️


More information at https://alectorsite.wordpress.com/corpus/ .

I made this repository public since the corpus is hardly accessible online. 

## Setup
Developed with ubuntu. 
You will need to have installed:
- Firefox Browser
- gecko driver
- selenium python package

You will also need to be registered on alector's website.

### Installation of gecko driver:
1. Download and extract the latest release (https://github.com/mozilla/geckodriver/releases). Example :
   - `wget https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux64.tar.gz` 
   - `tar -xvzf geckodriver-v0.29.1-linux64.tar.gz`
1. Make the file executable: `chmod +x geckodriver`
1. Create a folder where your geckodriver application will remain. Example: 
   - `mkdir /lib/geckodriver/`
1. Move the file to this newly created folder. Example: 
   - `mv geckodriver /lib/geckodriver/geckodriver`
1. Add the folder to PATH. Example: 
   - `PATH=$PATH:/lib/geckodriver/`

### Running the scraping script
Execute `python scrape_alector.py`. Give your credentials when prompted, and voilà!
