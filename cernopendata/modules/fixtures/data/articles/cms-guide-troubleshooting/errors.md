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

