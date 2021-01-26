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






pdb.set_trace()
