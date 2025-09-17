# Software Installation

Before starting:  
- Determine your operating system (Windows, macOS, Ubuntu Linux, etc.) and processor type (Intel/AMD or ARM). This can be found under **About** or **Properties** in your system settings.  
- Ensure you are connected to the Internet and have at least 3–4 GB of free disk space.  

---

## Visual Studio Code

(If you already use another editor such as Sublime Text, Notepad++, Spyder, or PyCharm, you may skip this step.)  
Download and install [Visual Studio Code](https://code.visualstudio.com/download) as your code editor. You can accept all default installation options.   

---

## Git

1. Create a [GitHub](https://github.com/signup) account if you don't already have one.

2. Create your first repository. In the upper-right corner of any page, select `+`, then click on `New repository`. In the `Repository name` box, type `cogsup-prog`. Make sure your repository is **Public** (this should be the case by default). You can accept the defaults for all the other options. Then, click on `Create repository`.

3. Create an access token—you will need this to update the repository with files and folders from your computer. In the upper-right corner, click on the icon representing your profile, then choose ```Settings```. Scroll down until you see ```Developer settings``` on the lefthand menu, and click on it. On the left, click on ```Personal access tokens```, then select ```Tokens (classic)```.  Click on the ```Generate new token``` button, then choose the first option (```Generate new token (classic)```). Select a token name under **Note** (e.g., "programming"), select ```No expiration``` under **Expiration** and check ```repo``` under **Select scope**. Click on ```Generate token```, then make sure to copy the generated token and paste it somewhere where you can retrieve it later.

4. Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for version control, following the platform-specific instructions at the link provided. 

> **Note (Windows only)** During the installation:  
> - In *Choosing the default editor used by Git*, select `Use Notepad`.  
> - In *Adjusting your PATH environment*, select `Use Git and optional Unix tools...`.  
> - In *Configuring the terminal emulator*, select `Use MinTTY`.  
> - You may keep defaults for all other options.  

5. After installation, open a terminal:  
- **Windows:** start **Git Bash**  
- **macOS:** open **Terminal** (via Spotlight: `⌘ + Space` → type `terminal`)  
- **Linux:** open **Terminal** (`Ctrl + Alt + T`)  

Configure your Git identity (replace placeholders with your own details):  

```bash
git config --global user.name "first_name last_name"
git config --global user.email "your_email"
git config --global core.editor nano
```

---

## Python

1. If Python ≥3.10 is not already installed, download it from [python.org](https://www.python.org).  

   - **Windows only:** during installation, check the option **“Add python.exe to PATH”**.  

2. Verify that Python runs from the command line:  

   - **Windows:**  
     - Start **Git Bash** and enter:  
       ```bash
       echo "alias python='winpty python.exe'" >> ~/.bash_profile
       ```  
       Press `Enter`, then close and reopen Git Bash.  

     - Type `python` and press `Enter`.  

        - If you see this:
         ```bash
         python: command not found
         ```  
         follow the instructions at [Real Python](https://realpython.com/add-python-to-path/) to add Python to your `PATH`.  

       - Otherwise, you should see:  
         ```bash
         Python 3.13.5 (main, Jun 16 2025, 17:39:28) [GCC 11.4.0] on Windows
         Type "help", "copyright", "credits" or "license" for more information.
         >>> 
         ```  
         Exit the interpreter by typing `quit()` and pressing `Enter`.  

   - **macOS / Linux:**  
     - Open **Terminal** (`⌘ + Space` → type `terminal` on macOS, `Ctrl + Alt + T` on Linux).  
     - Type `python` and press `Enter`.  
     - You should see a similar version message as above. Exit with `quit()`.  

---

## Basic Python Libraries

Install commonly used scientific libraries by running:  

```bash
pip install ipython jupyter numpy matplotlib pandas seaborn scikit-image
```

---

## Expyriment

[Expyriment](http://www.expyriment.org) is a Python library for programming cognitive psychology experiments.  

Install it with:  

```bash
pip install expyriment
```

Next, download the sample experiments and additional plugins in [Expyriment stash](https://github.com/expyriment/expyriment-stash/) by running:  

```bash
expyriment -D
```

When prompted:  
- Type `all`  
- Then type `master`  

to select all contents from the master branch.

---

## R and RStudio

- **R** is a programming language specialized for statistical data analysis. Download and install it from [CRAN](https://cran.rstudio.com/), accepting the default installation options.  
- **RStudio** is an Integrated Development Environment (IDE) for R that simplifies the use of RMarkdown. Download and install the free version of [RStudio Desktop](https://posit.co/download/rstudio-desktop/), also accepting the defaults.  

---

## Jupyter Notebook with R (IRkernel)

To run R inside Jupyter notebooks, you must install the **IRkernel**.  

1. Make sure Jupyter is already installed (see previous section).  
2. Open **R** (from RStudio or terminal) and run the following commands:  

```r
install.packages('tidyverse')
install.packages('IRkernel')
IRkernel::installspec(user = FALSE)
```

This makes R usable in Jupyter notebooks.

**Troubleshooting**
You might get one of two errors when running ```IRkernel::installspec(user = FALSE)```. 

If the error complains about not having admin access (typically, on Macs), open the terminal, type ```sudo R```, enter your computer password, then run ```IRkernel::installspec(user = FALSE)``` again. 

If the error complains that **jupyter-client** is not installed (typically on Windows):

- Press ```⊞ + R```, then type ```sysdm.cpl```.
- Go to **Advanced** → **Environment variables**.
- Under **User variables**, select **Path** → **Edit** → **New**, and paste: ```C:\Users\YOUR_USERNAME\AppData\Local\Programs\Python\Python313\Scripts``` (replace YOUR_USERNAME with your username).
- Restart Git Bash
- In Git Bash, enter:

```bash
jupyter --version
```

If you see a number, the troubleshooting worked. Open R and run ```IRkernel::installspec(user = FALSE)``` again.