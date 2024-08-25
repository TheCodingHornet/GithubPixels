import subprocess
from datetime import datetime, timedelta

# Dictionnaire des lettres (HIRE ME PLEASE !) avec une hauteur de 5 pixels
letters = {
    'H': [0b101, 0b101, 0b111, 0b101, 0b101],
    'I': [0b111, 0b010, 0b010, 0b010, 0b111],
    'R': [0b110, 0b101, 0b110, 0b101, 0b101],
    'E': [0b111, 0b100, 0b110, 0b100, 0b111],
    'M': [0b101, 0b111, 0b111, 0b111, 0b101],
    'P': [0b111, 0b101, 0b111, 0b100, 0b100],
    'L': [0b100, 0b100, 0b100, 0b100, 0b111],
    'A': [0b010, 0b101, 0b111, 0b101, 0b101],
    'S': [0b111, 0b100, 0b111, 0b001, 0b111],
    '!': [0b010, 0b010, 0b010, 0b000, 0b010],
    ' ': [0b000, 0b000, 0b000, 0b000, 0b000],
}

# Fonction pour créer un commit à une date donnée
def create_commit(date):
    subprocess.call(['git', 'commit', '--allow-empty', '--date', date, '-m', 'Automated commit'])

# Fonction pour dessiner une lettre avec des commits
def draw_letter_with_commits(letter, start_x, start_date):
    for row in range(5):  # Chaque lettre fait maintenant 5 lignes de hauteur
        for col in range(3):  # Chaque lettre fait 3 colonnes de largeur
            if (letters[letter][row] >> (2 - col)) & 1:  # Vérifier si le bit est à 1
                commit_date = start_date + timedelta(days=(row + 1))  # Du mardi au samedi
                time_of_day = datetime(commit_date.year, commit_date.month, commit_date.day, 9, 0)
                for i in range(6):  # 1 push toutes les 10 minutes (6 commits = 1 heure)
                    create_commit(time_of_day.strftime('%Y-%m-%dT%H:%M:%S'))
                    time_of_day += timedelta(minutes=10)

# Fonction pour dessiner le message avec des commits
def draw_message_with_commits(message, start_date):
    current_date = start_date
    for letter in message:
        draw_letter_with_commits(letter, 0, current_date)
        current_date += timedelta(weeks=1)  # Avancer d'une semaine pour chaque lettre

# Définir la date de début (par exemple, 1 an avant aujourd'hui)
start_date = datetime.now() - timedelta(weeks=52)

# Dessiner le message "HIRE ME PLEASE !" avec des commits
draw_message_with_commits("HIRE ME PLEASE !", start_date)
