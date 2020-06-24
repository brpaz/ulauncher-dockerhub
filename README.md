# Ulauncher Dockerhub

> Searches images from [Docker Hub](https://hub.docker.com/) directly from Ulauncher.

[![Ulauncher Extension](https://img.shields.io/badge/Ulauncher-Extension-yellowgreen.svg?style=for-the-badge)](https://ext.ulauncher.io/)
[![CI Status](https://img.shields.io/github/workflow/status/brpaz/ulauncher-dockerhub-extension/CI?color=orange&label=actions&logo=github&logoColor=orange&style=for-the-badge)](https://github.com/brpaz/ulauncher-dockerhub-extension)
[![license](https://img.shields.io/github/license/brpaz/ulauncher-dockerhub-extension.svg?style=for-the-badge)](https://github.com/brpaz/:ulauncher-dockerhub-extension/blob/master/LICENSE)

## Demo

![demo](demo.gif)

## Requirements

* [Ulauncher](https://github.com/Ulauncher/Ulauncher) > 5.0
* Python >= 3

## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```
https://github.com/brpaz/ulauncher-dockerhub-extension
```

## Usage

Type ```dockerhub <query>``` To search for images on DockerHub.

## Development

```
git clone https://github.com/brpaz/ulauncher-dockerhub-extension
make link
```

The `make link` command will symlink the cloned repo into the appropriate location on the ulauncher extensions folder.

To see your changes, stop ulauncher and run it from the command line with: `make dev`.

## Contributing

All contributions are welcome. Just open an issue and/or create a PR.

If you like my work, feel free to "Buy me a Coffee"

<a href="https://www.buymeacoffee.com/Z1Bu6asGV" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>

## License

MIT &copy; [Bruno Paz]
