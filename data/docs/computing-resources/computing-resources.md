The CERN Open Data files are large. Downloading all of them needs much disk space and network bandwidth. You do not need your own cluster to start. This page lists places where you can run an open data analysis.

The list is not complete. Each entry says who can use the resource and how to reach the data. The entries are not ranked. Choose the one that fits your task.

1. [Resources at a glance](#glance)
2. [Resources](#resources)
3. [How to reach the data](#data)
4. [Add your resource](#add)

## <a name="glance">Resources at a glance</a>

| Resource | Run by | Who can use it | Interface |
|---|---|---|---|
| [CERN SWAN](#swan) | CERN | People with a CERN account | Jupyter notebooks |
| [EOSC CERN Node](#eosc) | CERN | Researchers who sign in with an EOSC-compatible identity | Jupyter notebooks and workflows |
| [Nebraska coffea-casa](#nebraska) | University of Nebraska-Lincoln | Anyone (account request; Google sign-in works) | Jupyter notebooks |
| [EXPLORE](#explore) | University of Göttingen | Anyone (free registration) | Jupyter notebooks |
| [Google Colab and Binder](#free) | Google, the Binder project | Anyone | Jupyter notebooks |
| [Commercial cloud](#cloud) | Google, Amazon and others | Anyone (paid; some free credit) | Virtual machines |

## <a name="resources">Resources</a>

### <a name="swan">CERN SWAN</a>

[SWAN](https://swan.cern.ch) is the CERN service for analysis in Jupyter notebooks. It uses the CERN software stack and CERN storage. You need a CERN account. See the [SWAN documentation](https://swan.docs.cern.ch).

### <a name="eosc">EOSC CERN Node</a>

The [EOSC CERN Node](https://eosc.cern) gives researchers in the European Open Science Cloud access to a SWAN-based Virtual Research Environment and to REANA workflows. You do not need a CERN account. Access to the analysis services is granted on request. Read the Node pages for the current access rules and limits.

### <a name="nebraska">Nebraska coffea-casa</a>

The University of Nebraska-Lincoln runs an [analysis facility](https://coffea-opendata.casa/) for open data. You can request an account. You can sign in with Google, so you do not need an institutional affiliation.

The site has a cache (xcache) that gives faster access to the open data. See [How to reach the data](#data).

### <a name="explore">EXPLORE (University of Göttingen)</a>

[EXPLORE](https://punchlogin.goegrid.gwdg.de/) is an open data analysis platform at the Georg-August-Universität Göttingen. It is free and supported by PUNCH4NFDI. Students, teachers and other interested people can register without an affiliation to an LHC experiment or institution. The site offers tutorials for ATLAS Open Data, including the 13 TeV education releases and the research release in PHYSLITE format.

### <a name="free">Google Colab and Binder</a>

[Google Colab](https://colab.research.google.com) and [Binder](https://mybinder.org) are free and need no registration (Colab needs a Google account). They give a small amount of memory and disk space. Each session starts from an empty machine. You must install the software and get the data again each time. A single large file can be too big for Binder.

You can change an example notebook to run on these services. For example, the first cell of a notebook can install the packages it needs.

### <a name="cloud">Commercial cloud</a>

Commercial providers, for example [Google Cloud](https://cloud.google.com/) and [Amazon Web Services](https://aws.amazon.com/), rent virtual machines. Some providers give free credit to new users. You pay for the time you use and, in some cases, for data transfer. You must set up the software yourself.

## <a name="data">How to reach the data</a>

You can find the files you need with the [CERN Open Data client](https://cernopendata-client.readthedocs.io/en/latest/index.html). For ATLAS Open Data, you can also use [atlasopenmagic](https://opendata.atlas.cern/docs/atlasopenmagic/intro). These tools work on all the resources above.

You can use the files in two ways:

- **Download** a file once, then work on the local copy. This is usually the best choice on a slow connection. Use `xrdcp` with a file name that starts with `root://`, or `curl -O` with a file name that starts with `https://`. Which one is faster depends on your system.
- **Read remotely**, without a download. Give the full file name that starts with `root://`. This needs `xrootd` to be installed. It also depends on the network between CERN and your resource.

Some notes:

- Do not read many files in a fast loop. The portal limits the number of requests for each user. Download a file once and reuse it.
- On Google resources, `xrootd` is slow to build. It is easier to skip it and use `curl`.
- At Nebraska, use the xcache. In the file names you get from the client, replace `root://eospublic.cern.ch/` with `root://red-xcache1.unl.edu:1096/`. Access is faster, mainly for files that are already in the cache.

## <a name="add">Add your resource</a>

Do you run a service where people can analyse open data? To add it to this page, open a pull request or an issue in the [opendata.cern.ch repository](https://github.com/cernopendata/opendata.cern.ch). Please give:

- the name and the operator,
- who can use it and how they get access,
- the interface (for example Jupyter or batch),
- how the service reaches the data,
- a link to the documentation,
- a contact person.

A resource is suitable if people outside a collaboration can use it, it has public documentation, and someone has run an open data example on it.
