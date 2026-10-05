The CERN Open Data files are large. Downloading all of them needs much disk space and network bandwidth. You do not need your own cluster to start. This page lists places where you can run an open data analysis.

The list is not complete. Each entry says who can use the resource and how to reach the data. The entries are not ranked. Choose the one that fits your task.

Some resources that belong to an experiment have rules for their use. For example, Grid resources are normally for work that benefits the experiment. They are not for open data studies that lead to a publication outside the experiment. Read the usage policy of the resource, or ask the resource managers if you are not sure.

1. [Start on your laptop](#start)
2. [Resources at a glance](#glance)
3. [Resources](#resources)
4. [How to reach the data](#data)
5. [Add your resource](#add)

## <a name="start">Start on your laptop</a>

You do not need many CPU cores to learn from open data. Several analysis examples on the portal run in a few minutes. For example, the CMS Higgs-to-four-leptons example takes about 5 minutes. The ALICE transverse-momentum example takes about 1 minute. This is enough for many undergraduate students.

Use the resources below when you need more: many files, a full dataset or a research-grade analysis.

## <a name="glance">Resources at a glance</a>

The table shows who can use each resource.

| Resource | Run by | Who can use it | Interface |
|---|---|---|---|
| [CERN SWAN](#swan) | CERN | People with a CERN account | Jupyter notebooks |
| [CERN REANA](#reana) | CERN | People with a CERN account | Workflows |
| [EOSC and the CERN EOSC Node](#eosc) | CERN and other EOSC nodes | European researchers* | Jupyter notebooks and workflows |
| [Nebraska Coffea-Casa](#nebraska) | University of Nebraska-Lincoln | Anyone with an account. Google sign-in works | Jupyter notebooks |
| [EXPLORE](#explore) | University of Göttingen | Anyone (free registration) | Jupyter notebooks |
| [Google Colab and Binder](#free) | Google, the Binder project | Anyone | Jupyter notebooks |
| [Commercial cloud](#cloud) | Google, Amazon and others | Anyone. You pay, but some providers give free credit | Virtual machines |

\* You sign in with an identity that the European Open Science Cloud (EOSC) accepts. You do not need a CERN account.

## <a name="resources">Resources</a>

### <a name="swan">CERN SWAN</a>

[SWAN](https://swan.cern.ch) (Service for Web-based ANalysis) is the CERN service for analysis in Jupyter notebooks. It uses the CERN software stack and CERN storage. You need a CERN account. See the [SWAN documentation](https://swan.docs.cern.ch).

### <a name="reana">CERN REANA</a>

[REANA](https://reana.cern) (REusable ANAlyses) is the CERN service that runs analysis workflows. Many open data examples include a `reana.yaml` file, and you can launch them from the example gallery. You need a CERN account for the REANA instance at CERN. Other instances have their own access rules.

### <a name="eosc">The European Open Science Cloud and the CERN EOSC Node</a>

You can run an open data analysis on any node of the European Open Science Cloud (EOSC). The [CERN EOSC Node](https://eosc.cern) is one of them. It offers a SWAN-based Virtual Research Environment and REANA workflows. It runs the computation near the data, so data access is fast. On another node you can have more compute resources, but data access is slower over HTTP or XRootD.

You do not need a CERN account. You request access to the analysis services. Read the Node pages for the current access rules and limits.

### <a name="nebraska">Nebraska Coffea-Casa</a>

The University of Nebraska-Lincoln runs an [analysis facility](https://coffea-opendata.casa/) for open data. You can request an account. You can sign in with Google, so you do not need an institutional affiliation.

The site has a cache (xcache) that gives faster access to the open data. See [How to reach the data](#data).

### <a name="explore">EXPLORE (University of Göttingen)</a>

[EXPLORE](https://punchlogin.goegrid.gwdg.de/) is an open data analysis platform at the Georg-August-Universität Göttingen. It is free and supported by PUNCH4NFDI. Students, teachers and other interested people can register without an affiliation to an LHC experiment or institution. The site has tutorials for ATLAS Open Data. They cover the 13 TeV education releases and the research release in PHYSLITE format.

### <a name="free">Google Colab and Binder</a>

[Google Colab](https://colab.research.google.com) and [Binder](https://mybinder.org) are free and need no registration (Colab needs a Google account). They give a small amount of memory and disk space. Each session starts from an empty machine. You must install the software and get the data again each time. A single large file can be too big for Binder.

You can change an example notebook to run on these services. For example, the first cell of a notebook can install the packages it needs.

### <a name="cloud">Commercial cloud</a>

Commercial providers, for example [Google Cloud](https://cloud.google.com/) and [Amazon Web Services](https://aws.amazon.com/), rent virtual machines. Some providers give free credit to new users. You pay for the time you use and, in some cases, for data transfer. You must set up the software yourself.

## <a name="data">How to reach the data</a>

You can find the files you need with the [CERN Open Data client](https://cernopendata-client.readthedocs.io/en/latest/index.html). For ATLAS Open Data, you can also use [atlasopenmagic](https://opendata.atlas.cern/docs/atlasopenmagic/intro). These tools work on all the resources above.

You can use the files in two ways:

- **Download** a file once, then work on the local copy. This is usually the best choice on a slow connection. Use `xrdcp` with a file name that starts with `root://`. Or use `curl -O` with a file name that starts with `https://`. Which one is faster depends on your system.
- **Read remotely**, without a download. Give the full file name that starts with `root://`. You must install `xrootd` first. Speed also depends on the network between CERN and your resource.

Some software, for example ROOT and uproot, reads remotely by default when it can. This is also true for a file name that starts with `https://`. If you want a local copy, download the file first. In uproot, you can put `simplecache::` before the file name. Then uproot downloads the file when it reads it.

Some notes:

- Do not read the same file again and again in a loop. The portal limits the number of requests for each user. Download the file once and reuse it.
- On Google resources, `xrootd` is slow to build. It is easier to skip it and use `curl`.
- At Nebraska, use the xcache. In the file names you get from the client, replace `root://eospublic.cern.ch/` with `root://red-xcache1.unl.edu:1096/`. Reading is faster, mainly for files that are already in the cache.

## <a name="add">Add your resource</a>

Do you run a service where people can analyse open data? To add it to this page, open a pull request or an issue in the [opendata.cern.ch repository](https://github.com/cernopendata/opendata.cern.ch). Please give:

- the name and the operator,
- who can use it and how they get access,
- the interface (for example Jupyter or batch),
- how the service reaches the data,
- a link to the documentation,
- a contact person.

A resource is suitable if:

- people outside a collaboration can use it,
- it has public documentation,
- someone has run an open data example on it.
