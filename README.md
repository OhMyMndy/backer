# Backer!

Create multitrack backing tracks from Deezer playlists.


## Usage

```bash
podman build -t ohmymndy/backer:0.1 .

podman run --rm -it -v "$HOME/Music:/root/Music" ohmymndy/backer:0.1 <deezer-id> <deezer-arl> <search-term>

```