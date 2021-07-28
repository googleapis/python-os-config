# Changelog

### [1.3.2](https://www.github.com/googleapis/python-os-config/compare/v1.3.1...v1.3.2) (2021-07-28)


### Bug Fixes

* enable self signed jwt for grpc ([#101](https://www.github.com/googleapis/python-os-config/issues/101)) ([5f6c367](https://www.github.com/googleapis/python-os-config/commit/5f6c367753fb780f15ff38245b2c85387e01965e))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#97](https://www.github.com/googleapis/python-os-config/issues/97)) ([404adc3](https://www.github.com/googleapis/python-os-config/commit/404adc3419aaa40b0b66f55fc3ed92758287816b))


### Miscellaneous Chores

* release as 1.3.2 ([#102](https://www.github.com/googleapis/python-os-config/issues/102)) ([7c642b0](https://www.github.com/googleapis/python-os-config/commit/7c642b0eb32171275ee47db7ab64900176d0a4a1))

### [1.3.1](https://www.github.com/googleapis/python-os-config/compare/v1.3.0...v1.3.1) (2021-07-20)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#96](https://www.github.com/googleapis/python-os-config/issues/96)) ([022e149](https://www.github.com/googleapis/python-os-config/commit/022e149322e719465f1b0b66850def2b94c42eb1))

## [1.3.0](https://www.github.com/googleapis/python-os-config/compare/v1.2.0...v1.3.0) (2021-07-14)


### Features

* add always_use_jwt_access ([#88](https://www.github.com/googleapis/python-os-config/issues/88)) ([abb4837](https://www.github.com/googleapis/python-os-config/commit/abb48378d71deab058958c3b3b1efff5c253c99e))


### Bug Fixes

* disable always_use_jwt_access ([#92](https://www.github.com/googleapis/python-os-config/issues/92)) ([5d8a4bb](https://www.github.com/googleapis/python-os-config/commit/5d8a4bb9ef477f8fd81344fbd02631ac31660169))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-os-config/issues/1127)) ([#83](https://www.github.com/googleapis/python-os-config/issues/83)) ([b9fc494](https://www.github.com/googleapis/python-os-config/commit/b9fc4948a320fcf6a7154a2c7a1476cc78736c4d))

## [1.2.0](https://www.github.com/googleapis/python-os-config/compare/v1.1.0...v1.2.0) (2021-06-09)


### Features

* release as GA ([#46](https://www.github.com/googleapis/python-os-config/issues/46)) ([d5aece9](https://www.github.com/googleapis/python-os-config/commit/d5aece996ff225dc747e7c59978576bfcb79a3d1))
* support self-signed JWT flow for service accounts ([6fbaf4b](https://www.github.com/googleapis/python-os-config/commit/6fbaf4bb16b0bb381edf13957b85297c1659a206))
* add v1alpha ([#80](https://www.github.com/googleapis/python-os-config/issues/80)) ([493ac75](https://www.github.com/googleapis/python-os-config/commit/493ac75a5fec0185fa15415fe4feffe0c36ca7e9))


### Bug Fixes

* add async client to %name_%version/init.py ([6fbaf4b](https://www.github.com/googleapis/python-os-config/commit/6fbaf4bb16b0bb381edf13957b85297c1659a206))
* **deps:** add packaging requirement ([#72](https://www.github.com/googleapis/python-os-config/issues/72)) ([44e0947](https://www.github.com/googleapis/python-os-config/commit/44e09479922f8569b8d95657009e7c806eb101f9))


### Documentation

* fix sphinx identifiers ([#52](https://www.github.com/googleapis/python-os-config/issues/52)) ([940916d](https://www.github.com/googleapis/python-os-config/commit/940916de78ac19bea3f63f75ce073648f920c70b))

## [1.1.0](https://www.github.com/googleapis/python-os-config/compare/v1.0.0...v1.1.0) (2021-02-12)


### Features

* add `from_service_account_info` ([#31](https://www.github.com/googleapis/python-os-config/issues/31)) ([d8d921f](https://www.github.com/googleapis/python-os-config/commit/d8d921fc28d294039c574e4dc327fbe1caa27337))


### Bug Fixes

* remove client side receive limits  ([#29](https://www.github.com/googleapis/python-os-config/issues/29)) ([628ada4](https://www.github.com/googleapis/python-os-config/commit/628ada4004b1add04f5c2d95b9b1cad48616cf2c))

## [1.0.0](https://www.github.com/googleapis/python-os-config/compare/v0.1.2...v1.0.0) (2020-11-18)


### ⚠ BREAKING CHANGES

* rename attributes that conflict with builtins (#24)
    * `Instance.type` ->`Instance.type_`
    * `GcsObject.object` -> `GcsObject.object_`
    * `PatchInstanceFilter.all` -> `PatchInstanceFilter.all_`

### Features

* add async client ([#8](https://www.github.com/googleapis/python-os-config/issues/8)) ([33f46ba](https://www.github.com/googleapis/python-os-config/commit/33f46ba4aa34e066a70a5ad792254574b5985f83))
* add patch rollout to patch deployments ([#24](https://www.github.com/googleapis/python-os-config/issues/24)) ([4d8605e](https://www.github.com/googleapis/python-os-config/commit/4d8605e2d92af271b2c363490926689266c1d4b6))
* add common resource path helpers ([#24](https://www.github.com/googleapis/python-os-config/issues/24)) ([4d8605e](https://www.github.com/googleapis/python-os-config/commit/4d8605e2d92af271b2c363490926689266c1d4b6))
* make client transport public ([#24](https://www.github.com/googleapis/python-os-config/issues/24)) ([4d8605e](https://www.github.com/googleapis/python-os-config/commit/4d8605e2d92af271b2c363490926689266c1d4b6))
---
### [0.1.2](https://www.github.com/googleapis/python-os-config/compare/v0.1.1...v0.1.2) (2020-06-11)


### Bug Fixes

* remove duplicate version ([#6](https://www.github.com/googleapis/python-os-config/issues/6)) ([351b553](https://www.github.com/googleapis/python-os-config/commit/351b5531244bb207fc6696625dbeaf840e7a469f))

### [0.1.1](https://www.github.com/googleapis/python-os-config/compare/v0.1.0...v0.1.1) (2020-06-11)


### Bug Fixes

* fix documentation links ([#2](https://www.github.com/googleapis/python-os-config/issues/2)) ([9d71787](https://www.github.com/googleapis/python-os-config/commit/9d717874d310d40efdb8f2a316521ea90e8c0e63))

## 0.1.0 (2020-06-10)


### Features

* generate v1 ([5d1f582](https://www.github.com/googleapis/python-os-config/commit/5d1f582b5b02d128ef44120d285941805d234ec7))
