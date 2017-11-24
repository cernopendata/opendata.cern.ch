- The root password for CMS Open Data VM is `password`

- In some versions of VirtualBox, the CMS Open Data VM does not open correctly. This has happened for example for VirtulBox 5.0.32, but a more recent version is OK.

- xml files do not download correctly by clicking on "Download" e.g. `http://opendata.cern.ch/record/560/files/BuildFile.xml` in [record 560](/record/560)
Note that all files can be downloaded directly from the CMS Open Data VM terminal with wget e.g.
```
wget http://opendata.cern.ch/record/560/files/BuildFile.xml
```

- After the Windows update in June 2017, VirtualBox will not start. The problem has been fixed by the VirtualBox team and downloading the most recent version (5.1.22) from [the VirtualBox website](https://www.virtualbox.org/wiki/Downloads) solves the problem.


**I have trouble installing Virtualbox**
> read the FAQs. If it still fails, please contact your local system administrator

**When/after installing CERN VM, I get a message that my VM uses too much memory**
> reduce the memory allocated to the virtualbox

**When reading AOD data, I get write access warnings from eospublic on every file**
> this was a temporary 'feature' of a change in the eos software which has meanwhile been fixed. It does not affect the results.

**When reading AOD data, I get fatal access error messages from eospublic on specific files**
> According to the eos-admin team, disk access problems to eospublic may occur occasionally and are automatically corrected within a few hours. If the access problem to a particular file lasts longer than about a day send a mail to [eos-admins@cern.ch](mailto://eos-admins@cern.ch), providing the file name and a log of the error message.

**While running on AOD data, my job gets "killed" by the VM without any further explanation**

> You might have exceeded the VMs available memory (use the VMs monitoring tools to check whether memory is marginal). Try one of the following:
> - do not run anything else using a lot of memory (e.g. a web browser) on the VM in parallel
> - reduce memory usage of the job (and/or check for potential memory leak)
> - increase the memory allocated to the VM

**Any other problem you cannot solve yourself or with the help of your local administrator(s), not related to your local setup**

> kindly contact [opendata-support@cern.ch](mailto://opendata-support@cern.ch)

