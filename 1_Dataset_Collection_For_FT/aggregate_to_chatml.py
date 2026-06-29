import os
import json

def create_chatml_dataset(input_dir="Batch_Outputs", output_file="dataset_chatml.json"):
    """
    Agrège tous les fichiers JSON d'un dossier en un seul dataset au format ChatML.

    Args:
        input_dir (str): Le dossier contenant les fichiers batch JSON.
        output_file (str): Le nom du fichier de sortie.
    """
    final_dataset = []
    batch_files_count = 0
    total_examples_count = 0

    if not os.path.exists(input_dir):
        print(f"Erreur : Le dossier '{input_dir}' n'a pas été trouvé.")
        return

    print(f"Lecture des fichiers depuis le dossier '{input_dir}'...")

    # Parcourir tous les fichiers dans le dossier d'entrée
    for filename in sorted(os.listdir(input_dir)):
        if filename.endswith(".json"):
            batch_files_count += 1
            filepath = os.path.join(input_dir, filename)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                    # Vérifier si la clé 'examples' existe
                    if 'examples' in data and isinstance(data['examples'], list):
                        for example in data['examples']:
                            # Vérifier si la clé 'messages' existe dans l'exemple
                            if 'messages' in example:
                                final_dataset.append({"messages": example["messages"]})
                                total_examples_count += 1
                    else:
                        print(f"Avertissement : Le fichier '{filename}' ne contient pas de champ 'examples' valide.")

            except json.JSONDecodeError:
                print(f"Avertissement : Le fichier '{filename}' n'est pas un JSON valide et a été ignoré.")
            except Exception as e:
                print(f"Erreur inattendue lors de la lecture de '{filename}': {e}")

    # Sauvegarder le dataset final
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(final_dataset, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Erreur lors de la sauvegarde du fichier '{output_file}': {e}")
        return

    # Afficher le résumé
    print("\n--- Résumé de l'agrégation ---")
    print(f"Nombre de fichiers batch traités : {batch_files_count}")
    print(f"Nombre total d'exemples agrégés : {total_examples_count}")
    print(f"Dataset final sauvegardé dans : '{output_file}'")

    # Afficher un aperçu du premier exemple
    if final_dataset:
        print("\n--- Aperçu du premier exemple ---")
        print(json.dumps(final_dataset[0], ensure_ascii=False, indent=2))

if __name__ == "__main__":
    create_chatml_dataset()
