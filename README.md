
<p align="center">
  <a href="https://github.com/rmdlv/elpy">
    <img src="https://github.com/rmdlv/elpy/raw/main/docs/logo.png" width="175px" style="display: inline-block; border-radius: 5px">
  </a>
</p>
<h1 align="center">
  elpy
</h1>

> Pure Python EchoLink library
> 
## Features

 - [x] Directory client
 - [ ] QSO client
 - [ ] EchoLink proxy support

## Installation

```shell
pip install -U https://github.com/rmdlv/elpy/archive/refs/heads/main.zip
```

## Directory client

```python
from elpy import DirectoryClient

client = DirectoryClient(
	callsign="RA0SMS",
	password="SamplePass123",
	description="elpy client for Python",
	host="asia.echolink.org",
	port=5200,
)

client.make_online()
print(client.get_stations())
```

