import tkinter as tk
from tkinter import messagebox
from tacheDB import create_task, get_all_tasks, update_task, delete_task

# Fenêtre principale
fenetre = tk.Tk()
fenetre.title("Ma Liste de Taches")
fenetre.geometry("800x500")
fenetre.configure(bg="lightblue")

# Variables globales
tache_selectionnee = None
liste_active = None  # savoir de quelle liste vient la sélection

# Fonction pour ajouter une tache
def ajouter_tache():
    texte = champ_texte.get()
    if texte == "":
        messagebox.showwarning("Attention", "Veuillez écrire une tache")
        return
    
    try:
        create_task(texte, "Medium", "En cours")
        champ_texte.delete(0, tk.END)
        afficher_taches()
        messagebox.showinfo("Succès", "Tâche ajoutée!")
    except Exception as e:
        messagebox.showerror("Erreur", "Problème: " + str(e))

# Fonction pour afficher les taches
def afficher_taches():
    liste_taches_encours.delete(0, tk.END)
    liste_taches_terminees.delete(0, tk.END)
    
    try:
        taches = get_all_tasks()
        for tache in taches:
            id, contenu, status, priorite = tache
            texte_affiche = f"[{id}] {contenu} - {status} - {priorite}"
            if status == "En cours":
                liste_taches_encours.insert(tk.END, texte_affiche)
            elif status == "Terminée":
                liste_taches_terminees.insert(tk.END, texte_affiche)
    except Exception as e:
        messagebox.showerror("Erreur", "Problème: " + str(e))

# Fonction pour sélectionner une tache
def selectionner_tache():
    global tache_selectionnee, liste_active
    selection_encours = liste_taches_encours.curselection()
    selection_terminees = liste_taches_terminees.curselection()

    if selection_encours:
        tache_selectionnee = selection_encours[0]
        liste_active = "En cours"
        messagebox.showinfo("Sélection", "Tâche en cours sélectionnée")
    elif selection_terminees:
        tache_selectionnee = selection_terminees[0]
        liste_active = "Terminée"
        messagebox.showinfo("Sélection", "Tâche terminée sélectionnée")
    else:
        messagebox.showwarning("Attention", "Veuillez choisir une tâche")

# Fonction pour supprimer une tache
def supprimer_tache():
    global tache_selectionnee, liste_active
    if tache_selectionnee is None or liste_active is None:
        messagebox.showwarning("Attention", "Choisissez une tâche")
        return
    
    try:
        taches = get_all_tasks()
        if liste_active == "En cours":
            tache = [t for t in taches if t[2] == "En cours"][tache_selectionnee]
        else:
            tache = [t for t in taches if t[2] == "Terminée"][tache_selectionnee]
        
        id_tache = tache[0]
        delete_task(id_tache)
        afficher_taches()
        tache_selectionnee = None
        liste_active = None
        messagebox.showinfo("Succès", "Tâche supprimée!")
    except Exception as e:
        messagebox.showerror("Erreur", "Problème: " + str(e))

# Fonction pour marquer comme terminée
def terminer_tache():
    global tache_selectionnee, liste_active
    if tache_selectionnee is None or liste_active is None:
        messagebox.showwarning("Attention", "Choisissez une tâche en cours")
        return
    
    try:
        taches = get_all_tasks()
        if liste_active == "En cours":
            tache = [t for t in taches if t[2] == "En cours"][tache_selectionnee]
            id_tache, contenu, status, priorite = tache
            update_task(id_tache, contenu, priorite, "Terminée")
            afficher_taches()
            messagebox.showinfo("Succès", "Tâche terminée!")
        else:
            messagebox.showwarning("Attention", "Cette tâche est déjà terminée")
    except Exception as e:
        messagebox.showerror("Erreur", "Problème: " + str(e))

# Interface utilisateur
titre = tk.Label(fenetre, text="Ma Liste de Taches", font=("Arial", 20, "bold"), bg="lightblue")
titre.pack(pady=10)

# Champ de saisie
frame_saisie = tk.Frame(fenetre, bg="lightblue")
frame_saisie.pack(pady=10)

label_texte = tk.Label(frame_saisie, text="Nouvelle tâche:", font=("Arial", 12), bg="lightblue")
label_texte.pack(side=tk.LEFT)

champ_texte = tk.Entry(frame_saisie, font=("Arial", 12), width=30)
champ_texte.pack(side=tk.LEFT, padx=5)

bouton_ajouter = tk.Button(frame_saisie, text="Ajouter", command=ajouter_tache, bg="green", fg="white", font=("Arial", 10))
bouton_ajouter.pack(side=tk.LEFT, padx=5)

# Cadre pour séparer les deux listes
frame_listes = tk.Frame(fenetre, bg="lightblue")
frame_listes.pack(pady=10)

# Liste des tâches en cours
frame_encours = tk.Frame(frame_listes, bg="lightblue")
frame_encours.pack(side=tk.LEFT, padx=20)

label_encours = tk.Label(frame_encours, text="Tâches en cours:", font=("Arial", 14, "bold"), bg="lightblue")
label_encours.pack()

liste_taches_encours = tk.Listbox(frame_encours, font=("Arial", 11), height=15, width=40)
liste_taches_encours.pack(pady=5)

# Liste des tâches terminées
frame_terminees = tk.Frame(frame_listes, bg="lightblue")
frame_terminees.pack(side=tk.LEFT, padx=20)

label_terminees = tk.Label(frame_terminees, text="Tâches terminées:", font=("Arial", 14, "bold"), bg="lightblue")
label_terminees.pack()

liste_taches_terminees = tk.Listbox(frame_terminees, font=("Arial", 11), height=15, width=40)
liste_taches_terminees.pack(pady=5)

# Boutons d'action
frame_boutons = tk.Frame(fenetre, bg="lightblue")
frame_boutons.pack(pady=10)

bouton_selectionner = tk.Button(frame_boutons, text="Sélectionner", command=selectionner_tache, bg="blue", fg="white", font=("Arial", 10))
bouton_selectionner.pack(side=tk.LEFT, padx=5)

bouton_terminer = tk.Button(frame_boutons, text="Terminer", command=terminer_tache, bg="orange", fg="white", font=("Arial", 10))
bouton_terminer.pack(side=tk.LEFT, padx=5)

bouton_supprimer = tk.Button(frame_boutons, text="Supprimer", command=supprimer_tache, bg="red", fg="white", font=("Arial", 10))
bouton_supprimer.pack(side=tk.LEFT, padx=5)

bouton_actualiser = tk.Button(frame_boutons, text="Actualiser", command=afficher_taches, bg="purple", fg="white", font=("Arial", 10))
bouton_actualiser.pack(side=tk.LEFT, padx=5)

# Charger les tâches au démarrage
afficher_taches()

# Lancer l'application
fenetre.mainloop()
