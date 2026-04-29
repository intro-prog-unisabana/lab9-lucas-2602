# Write your code here!
class Song:
    def __init__(self, name, artist, length):
        self.name = name
        self.artist = artist
        self.length = length
    def get_length_in_seconds(self):
        cancion_en_minutos = self.length
        cancion_en_segundos = cancion_en_minutos * 60
        return cancion_en_segundos
    def __str__(self):
        return f"'{self.name}' by {self.artist} ({self.length})"