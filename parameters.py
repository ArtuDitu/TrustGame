# import libraries
from psychopy import visual
import os


#import pyxid2 as pyxid2
#######


#Cedrus
# get a list of all attached XID devices
#devices = pyxid2.get_xid_devices()
#dev = devices[0] # get the first device to use
#dev.reset_base_timer()
#dev.reset_rt_timer()

# example use:     dev.activate_line(bitmask=99)


# Participant number stored in a variable
participant_number = 659
# number of trials
TG_trials = 5
# start condition
start_condition = 'fair'
appraisal = True
understood = False

###TG parameters
min_investment_p = 0
max_investment_p = 10 # this is also initial budget
previous_investment = None  # To track investment from the previous iteration



directory = 'data'
# Create a file with the participant number in its name
tg_file_name = f"TG_{participant_number}.csv"
tg_file_path = os.path.join(directory, tg_file_name)

# Define window dimensions (update this for your setup or leave None for full-screen mode)
window_width = 1960
window_height = 1080


# Create a PsychoPy window
win = visual.Window(
    size=(window_width, window_height),  # Adjust to match your monitors' combined resolution
    color=[0.5, 0.5, 0.5],  # Gray background
    units="norm",  # Normalized units for scalability (-1 to 1 range)
    pos = (0,0),
    allowGUI=False
)
win.mouseVisible = False

directory = 'data'
# Create a file with the participant number in its name
esm_file_name = f"esm_{participant_number}.csv"
esm_file_path = os.path.join(directory, esm_file_name)

key_mappings = {
    'up': 'up',         # Up arrow key
    'down': 'down',     # Down arrow key
    'confirm': 'return' # Enter/Return key for confirmation
}


### texts

welcome_text = 'Witamy\n\n Wciśnij SPACE by kontynuować'
return_text_p = 'Twój powiernik zwrócił dla Ciebie:'

## instructions
instructions1 = 'W tym badaniu będziesz wielokrotnie inwestował sumy pieniędzy z dwoma innymi partnerami (JACKIEM i MIRKIEM). \n Za każdym razem gdy powierzysz sume jednemu z powierników ta suma będzie potrojona\n\n Następnie dowiesz się ile ta inwestycja zarobiła oraz co najważniejsze ile twój powiernik (Jacek albo Mirek) zdecydowali się dla Ciebie zwrócić\n\nWciśnij SPACE by kontynuować'
instructions2 = 'By zdecydować ile chcesz zainwestować będziesz musiał podać liczbę pomiędzy 0 i 10 oraz wcisnąć ENTER by ją potwierdzić.\n\n Wciśnij SPACE by spróbować'
instructions3 = 'Teraz się dowiesz ile ta inwestycja zarobiła pieniędzy.\n\n Wciśnij SPACE by kontynuować'
instructions4 = 'Teraz się dowiesz ile twój powiernik zdecydował się tobie zwrócić.\n\n Wciśnij SPACE by kontynuować'
instructions5 = 'To już całe instrukcje. Pamiętaj, musisz podjąć decyzje ile chcesz zainwestować i po tym dowiesz się ile twój powiernik zdecydował Ci sie zwrócić.\n\n Jeśli zrozumiałeś całe instrukcje to wciśnij SPACE by kontynować.\n\n Jeśli chciałbym zobaczyć instrukje jeszcze raz wciśnij ENTER'

# esm initial text
esm_start_text = 'W tej części badania zostaną wyświetlone słowa, które opisują rożne uczucia i emocje.\n\nPrzy każdym z nich prosimy, nie zastanawiając się długo nad odpowiedzią, zaznaczyć na skali 1 (Zdecydowanie nie) do 7 (Zdecydowanie tak), czy czujesz się w określony sposób.\n\nWybierz odpowiedź (w góre wciśnij UP, w dół wciśnij DOWN) i potwierdź wciskając ENTER\n\n\nNaciśnij teraz SPACE by kontynuować'

# esm others text
esm_others_text = 'W tej części badania zostaną wyświetlone słowa odnoszące się do sposobu, w jaki można odbierać innych ludzi.\n\nPrzy każdym z nich prosimy, nie zastanawiając się długo nad odpowiedzią, zaznaczyć na skali 1 (Zdecydowanie nie) do 7 (Zdecydowanie tak), czy dane określenie wydaje Ci się pasować do osoby z drugiego pokoju.\n\nWybierz odpowiedź (w góre wciśnij UP, w dół wciśnij DOWN) i potwierdź wciskając ENTER\n\n\nNaciśnij teraz SPACE by kontynuować'

# esm interaction text
esm_interaction_text= 'Teraz wyświetlone zostaną stwierdzenia, które mogą ale nie muszą pasować do interakcji, w której się znajdujesz\n\nZaznacz proszę na skali od 1 (Zdecydowanie nie) do 5 (Zdecydowanie tak), czy przedstawione stwierdzenie pasuje do tej interakcji.\n\nWybierz odpowiedź (w góre wciśnij UP, w dół wciśnij DOWN) i potwierdź wciskając ENTER\n\n\nNaciśnij teraz SPACE by kontynuować'

# esm activity text
esm_activity_text = 'Teraz wyświetlone zostaną zdania dotyczące różnych stanów lub aktywności\nZaznacz proszę na skali od 1 (Zdecydowanie nie) do 7 (Zdecydowanie tak), czy występowały one u Ciebie w ciągu ostatnich 15 minut.\n\nWybierz odpowiedź (w góre wciśnij UP, w dół wciśnij DOWN) i potwierdź wciskając ENTER\n\n\nNaciśnij teraz SPACE by kontynuować'

#esm end text
esm_end_text = 'Dziękujemy za wypełnienie ankiety! \n\n\nPoczekaj na dalsze instrukcje od osoby prowadzącej badanie.'

# esm question texts
#feeling text
feeling_text = 'Czy czujesz się teraz... \n\n'
#feelings
feelings = ['radosny/a?', 'odprężony/a?', 'związany/a z innymi?', 'spokojny/a', 'akceptowany/a', 'zestresowany/a', 'zaniepokojony/a' ]
feelings2 = ['samotny/a', 'wykluczony/a']


# others text
others_text = 'Druga osoba wydaje mi się... \n\n'
#others opinions
others_opinions = ['godna zaufania', 'nieprzyjemna', 'nieszczera', 'oceniająca', 'akceptująca', 'przyjazna']

#interaction text
interaction_text = 'Na ile zgadzasz się z poniższymi stwierdzeniami w odniesieniu do aktualnej interakcji:  \n\n'
# interaction opinions
interaction_opinions =['To, co każde z nas zrobiło w tej sytuacji, wpływa na drugą osobę', 'Każda z osób mogła uzyskać pożądane cele.', 'Cokolwiek każde z nas zrobiło, w tej suytuacji, nie miałoby to wpływu na drugą osobę.', 'Nasz cele w tej sytuacji są sprzeczne.']

interaction_opinions_person = ['Kto miał większą możliwość wpływania na na przebieg sytuacji?', 'Kto miał najmniejszy wpływ na wynik tej sytuacji?' ]

#activity text
activity_text = 'W trakcie interakcji... \n\n'
#activity opinions
activity_opinions = ['przyjmowałem/am perspektywę drugiej osoby.', 'odczuwałem/am troskę i współczucie.', 'odczuwałem/am dystans i chłód', 'skupiałem/am się na swojej perspektywie.']

# List of words to display
words_7 = ["Zdecydowanie nie", "Nie", "Raczej nie", "Ani tak, ani nie", "Raczej tak", "Tak", "Zdecydowanie tak"]
words_5 = ["Zdecydowanie nie", "Raczej nie", "Ani tak, ani nie", "Raczej tak", "Zdecydowanie tak"]
words_person = ["Zdecydowanie druga osoba", "Raczej druga osoba", "Ani druga osoba, ani ja", "Raczej ja", "Zdecydowanie ja"]

text_block1and3 = 'W tej części będziesz inwestował z JACKIEM\n\n Naciśnij teraz SPACE by kontynuować \n\n Inwestycje się rozpoczną gdy JACEK będzie gotowy'
text_block2and4 = 'W tej części będziesz inwestował z MIRKIEM\n\n Naciśnij teraz SPACE by kontynuować \n\n Inwestycje się rozpoczną gdy MIREK będzie gotowy'