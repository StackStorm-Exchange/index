# StackStorm Exchange Index

Hello, my friend. Stay awhile and listen.

I am going to tell you all about the StackStorm Exchange Index, a sacred tome
holding detailed accounts of every StackStorm pack that the Order deemed
worthy of the world to see.

### Structure

The index is currently compiled into a single JSON object and stored as a file:
[v1/index.json](https://github.com/StackStorm-Exchange/index/blob/master/v1/index.json).
Packs are identified by names, and their metadata is copied as is from the
`pack.yaml` files. `repo_url` is the only property that is stored in the index
but not in `pack.yaml`; it contains, quite unsurprisingly, a URL for the git
repository to clone the pack from.

This is a simplified index example:

```
{
  "aws": {
    "name": "aws",
    "version": "0.0.1",
    <other metadata from pack.yaml>
    "repo_url": "https://github.com/StackStorm-Exchange/stackstorm-aws/"
  },
  "sensu": {
    "name": "sensu",
    "version": "0.3.7",
    <other metadata from pack.yaml>
    "repo_url": "https://github.com/StackStorm-Exchange/stackstorm-sensu/"
  }
}
```

### Rebuilding the index

Rebuilding of the StackStorm Exchange index is performed on every `pack.yaml`
change in the `master` branch of a tracked StackStorm Exchange pack. The
rebuild is automatic and rarely takes more than a couple minutes. If your PR
has been merged for some time, and the index has not been updated, please
raise an issue.

Our [CI repository](https://github.com/StackStorm-Exchange/ci) contains the
necessary scripts, and you can take a peek to see how the rebuild works.
The repository is public, so the whole process is fully transparent!

### Building your own index (advanced)

The `index_urls` parameter inside `st2.conf` supports a comma-separated list
of index files. Building your own index might be useful if you have a bunch
of internal packs: you would be able to keep track of them in a centralized
way and make them easily discoverable in your StackStorm instances.

Additionally, if your StackStorm deployment is subject to a security policy
or heavily firewalled, you can clone the necessary packs to an internal
server and host your own index with modified `repo_url`s.
