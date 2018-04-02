1. [How to install VirtualBox](#vbox)
2. [Create a VM](#create)
3. [Configure a VM](#configure)


## <a name="vbox">Step 1: Installing VirtualBox</a>

VirtualBox is a free, open source and multiplatform application to run virtual machines: you can [download](https://www.VirtualBox.org/wiki/Downloads) the package for your platform from the Downloads page.

You will need administrative privileges ("root" privileges) on every platform to perform the installation of VirtualBox.

Note: the latest tested version of VirtualBox working with CernVM is 4.3.14\. If you have troubles with the latest verion of VirtualBox, pick that one: the full history of VirtualBox versions is available [on a different page.](https://www.VirtualBox.org/wiki/Download_Old_Builds)

## <a name="create">Step 2: Creating a Virtual Machine</a>

Go on the [CernVM downloads page](http://cernvm.cern.ch/portal/downloads) and download the appropriate version: you must pick the OVA x86_64 for VirtualBox.

<img src="/static/docs/virtual-machines-alice/1.png" width="50%">

Now open VirtualBox. Select **Import Appliance**... from the **File** menu.

<img src="/static/docs/virtual-machines-alice/2.png" width="70%">

From the import dialog, select the OVA file you have just downloaded.

<img src="/static/docs/virtual-machines-alice/3.png" width="70%">

In the Appliance settings dialog, change the following values:

* change the name to whatever you want in order to recognise your VM in the future
* increase the RAM to 2048 MB
* check "Reinitialize the MAC address of all network cards"
You can compare your settings with the picture below.

<img src="/static/docs/virtual-machines-alice/4.png" width="70%">

Click **Import**. You will have now the CernVM virtual machine available in the list of virtual machines. Select it, then press the **Start** button to boot it.

<img src="/static/docs/virtual-machines-alice/5.png" width="70%">

Let CernVM finish the boot process. As you might have noticed, the OVA file you have downloaded is less than 20 MB in size: in fact, it does not contain the operating system's components, which are downloaded on demand as soon as you access them.

For this reason, the first boot might take longer. Afterwards, the main components will be accessed from the cache.

Note: CernVM needs Internet connectivity to run. You cannot run CernVM when you are offline.

## <a name="configure">Step 3: Configuring a Virtual Machine</a>

When the virtual machine is started, it is a generic virtual machine, not configured to any specific purpose. It does not even have users, thus you still cannot log in: you have to specialise it by applying a configuration.

This process is called contextualisation, and can be performed entirely using a web browser: just start by navigating to the CernVM Online web site.

The first time you connect you need to register: the procedure takes seconds. Click on the register link:

<img src="/static/docs/virtual-machines-alice/6.png" width="50%">

Complete the registration form. You must provide a valid email address: you will receive a confirmation email for activating the account.

<img src="/static/docs/virtual-machines-alice/7.png" width="60%">

**Note:** please make sure that the "captcha" is filled correctly.

Once you have registered, you can go back to the login page and provide your credentials.

In this example, we are looking for the **ALICE analysis** configuration for the **ALICE** experiment: adapt the example to the configuration you wish to apply.

From the top menu, click on **Marketplace (Step A)**, then on the bottom right click on **ALICE (Step B)**. From the list of available configurations, select **ALICE analysis (Step C)** as shown in the picture.

<img src="/static/docs/virtual-machines-alice/8.png" width="70%">

When the configuration is selected, click the **Pair button (Step D)**: a six-digit number will appear on the screen, as shown in the picture:

<img src="/static/docs/virtual-machines-alice/9.png" width="70%">

Don't close this web page. Go instead to VirtualBox, where you have the login screen of CernVM. At the login screen, type the pound sign (#) followed by the six digits (no spaces).

<img src="/static/docs/virtual-machines-alice/10.png" width="70%">

The virtual machine will download the configuration automatically, and the web page on CernVM Online will update automatically.

<img src="/static/docs/virtual-machines-alice/11.png" width="70%">

Your CernVM virtual machine should now present a graphical interface: you can start using it immediately. Enjoy!
