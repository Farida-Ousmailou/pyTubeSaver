# Projet "pytubesaver"
# module pytube
# module re
from re import match
from pytube import YouTube

"""Ce programme utilise les modules Pytube et re pour créer des fonctions permettant de télécharger des vidéos depuis 
YouTube et d'extraire leurs métadonnées vers un chemin de stockage prédéfini."""

#Fonction permettant de le téléchargement
def Download_video(youtube_video, path):
    try:
        #Choix de la plus haute résolution
        stream = youtube_video.streams.get_highest_resolution()
        print("Stream vidéo: ", stream)

        #Information sur le niveau de progression du téléchargement
        def Download_progress(stream, chunk, bytes_remaining):
            bytes_downloaded = stream.filesize - bytes_remaining
            pourcentage = bytes_downloaded * 100 / stream.filesize
            print(f"Progression du téléchargement: {int(pourcentage)}%")

        #Téléchargement de la vidéo avec l'avénénement de la progression
        print("Téléchragement en cours...")
        youtube_video.register_on_progress_callback(Download_progress)
        stream.download(path)
        print("Fin de téléchargement")

    except:
        print("Une erreur s'est produites")

#Fonction permettant l'affichage des données de la vidéo
def Affichage_des_metadonnees (youtube_video):
    try:
        print("Titre de la vidéo: ", youtube_video.title)
        print("Nombre de vues: ", youtube_video.views)
        print("Auteur: ", youtube_video.author)
        print("Description: ", youtube_video.description)
    except:
        print("Impossible d'afficher les métadonnées")

#fonction permettant le recueil de l'url
def get_youtube_url():
    url_video = ""
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    is_url_matched = None
    while is_url_matched == None:
        url_video = input("Entrez l'URL de la vidéo YouTube : ")
        is_url_matched = match(youtube_regex, url_video)
        if is_url_matched == None:
            print("L'url : "+url_video+" n'est pas un lien video YouTube. Veuillez essayer ...")
    return url_video


#fonction permettant le recueil du chemin de stockage
def get_chemin():
    path = ""
    path_regex = r'(?:\/(?:[^/\0]+\/)*[^/\0]+)?'
    is_path_matched = None
    while is_path_matched is None:
        path = input("Entrez le chemin du répertoire de destination : ")
        is_path_matched = match(path_regex, path)
        if is_path_matched is None:
            print("Le chemin : " + path + " n'est pas bon. Veuillez essayer à nouveau...")
    return path

#Fonction main début de l'exécution du programme
def main():
    #Demande à l'utilisateur l'url et l'emplacement de la vidéo sur son repertoire
    url_video = get_youtube_url()
    path = get_chemin()

    #Création d'objet YouTube avec l'URL de la vidéo
    try:
        youtube_video = YouTube(url_video)
        # Appel de la fonction Affichage des métandonnées
        Affichage_des_metadonnees(youtube_video)

        # Appel de la fonction Download vidéo
        Download_video(youtube_video, path)
    except Exception as e:
        error_message = str(e)
        if error_message.__contains__("regex_search"):
            print("Veuillez saisir un url correct")
        else:
            print("Failed: " + str(e))



if __name__ == "__main__":
    main()

