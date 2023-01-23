<p align="center">
    <h1 align="center"/> Python FTP Cloud </h1>
</p>

<p align="center">
    <a href="/docs/readme_es.md"> Español </a>
</p>


## Developers
<table align="center">
<tbody>
<tr>
<td align="center"><a href="https://github.com/ImMamey" rel="nofollow"><img src="https://avatars.githubusercontent.com/u/32584037?v=4" width="150px;" alt="" style="max-width:100%;"><br><sub><b>Mamey</b></sub></a><br><a href="https://github.com/ImMamey/python-personal-cloud-ftp/commits?author=ImMamey" title="Commits"><g-emoji class="g-emoji" alias="book" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4d6.png">📖</g-emoji></a></td>
</tr>
</tbody>
</table>

---


## Description
 A small and lightweight local-network based file storage server (Google Drive-like) made with python3, pyQT5, pyftplib, and Docker (Optional, can run without docker).


---
## Features
* Upload/download/Delete files in your local network.
* Can make multiple separated Users.
* Can create up to 2 admin accounts to manage and create users.

---


## Requirements
#### Dependencies:
* [Python 3.10+](https://www.python.org/downloads/)
* [ftpdlib](https://github.com/giampaolo/pyftpdlib)
* [PyQT5](https://pypi.org/project/PyQt5/)
* [Pydantic](https://docs.pydantic.dev/)
* [Sqlite3](https://docs.python.org/3/library/sqlite3.html)
* Pyside2
#### Dev dependencies and extras:
* [PyQT5 Designer](https://build-system.fman.io/qt-designer-download) (To edit the front end)
* [Mypy](http://mypy-lang.org/) (Optional: for debbugging only)
---
## Installation

1. Download and install [Python 3.10.8](https://www.python.org/downloads/)
2. Download (or clone) this repository.
3. Once the repository is opened, access to the directory through terminal/cmd.

##### With poetry:
4. Run `poetry install` in the repository to install all the dependencies.
##### Without poetry:
4. Run `pip install -U mypy python-dotenv PyQt5 pyside2 pyftpdlib pydantic pywin32`.
>    You would need to install the exact versions that are described in the `project.toml`
---

## Running the Server
#### From your IDE
* Click on `src/server/app.py` -> Run
#### From lastest .exe:
* Get the lastest [server release]() and execute it

## Running a user client
#### From your IDE
* Click on `src/client/client.py`-> Run
#### From lastest .exe:
* Get the lastest [client release]() and execute it
---


## References
* [Requirements (wiki-docs)]()


---
## License
* [GPL-3.0 license](https://github.com/ImMamey/python-personal-cloud-ftp/blob/master/LICENSE.md)

