# Changelog

Released versions are immutable. A correction to a released version is a new
patch version. This file records *why* each version exists.

## v1

Initial release.

Measured under `scaffold-balanced-5seed@1`. Two scaffold groups hold
2700 of the 5823 compounds between them, more than the validation fold's
capacity, so the shuffle packer starves that fold and cannot measure this
dataset at all.

Two endpoints. A compound that kills the cell moves the reporter as a
consequence, so the viability counter-screen ships as its own output. It carries
a null where it made no call, and each output is fit on the compounds it labels.

Signature 1: `hsr_activation` and `hsr_cytotox`.
