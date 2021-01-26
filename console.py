import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_repository.delete_all()

artist1 = Artist("Haim")
artist_repository.save(artist1)
artist2 = Artist("Beyonce")
artist_repository.save(artist2)
artist3 = Artist("Gorillaz")
artist_repository.save(artist3)

# res = artist_repository.select_all()
# for artist in res:
#     print(artist.__dict__)

album1 = Album("Days Are Gone", artist1, "Pop Rock")
album_repository.save(album1)
album2 = Album("Something to Tell You", artist1, "Pop Rock")
album_repository.save(album2)
album3 = Album("Women in Music Pt. III", artist1, "Soft Rock")
album_repository.save(album3)





pdb.set_trace()
