Bundle Tools
================

This a set of tools that helps me (and hopefully you) to manage
Sugar bundles updates.

What problems does it solve?
----------------------------

* Provide Sugar bundles updates, with minimal requirements.
* Upload bundles to the server.
* Update microformat file.

How can I use it?
-----------------

0. Get latest bundletools bits.

    ```
    git clone https://github.com/tchx84/bundletools.git
    cd bundletools
    ```

1. Create or download your configuration recipe.

    ```
    cp etc/bundles.json.example etc/bundles.json
    vim etc/bundles.json
    ```

    or

    ```
    cp ~/Downloads/bundles.json etc/bundles.json
    ```

2. Update one or more bundles, to a specific bundles repository.

    ```
    ./update.sh arm-addons Letters-25.xo
    ```

    It will automatically upload the bundle to the corresponding
    directory in the server and it will also re-generate the
    microformat file.

3. Done.
