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

album4 = Album("Dangerously In Love", artist2, "R&B")
album_repository.save(album4)
album5 = Album("B'Day", artist2, "R&B")
album_repository.save(album5)
album6 = Album("I Am...Sasha Fierce", artist2, "R&B")
album_repository.save(album6)
album7 = Album("4", artist2, "R&B")
album_repository.save(album7)
album8 = Album("Beyonce", artist2, "R&B")
album_repository.save(album8)
album9 = Album("Lemonade", artist2, "R&B")
album_repository.save(album9)

album10 = Album("Demon Days", artist3, "Alternative Rock")
album_repository.save(album10)
album11 = Album("Plastic Beach", artist3, "Pop")
album_repository.save(album11)
album12 = Album("Humanz", artist3, "Electropop")
album_repository.save(album12)

album_repository.delete_all()

pdb.set_trace()
