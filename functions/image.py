from os import system, listdir

u_cookie_value = "1aigEgSX54WIShV1hF5oz6qL-elAgOWc7muGQ9p3K0QptKBZ2ZjiFpcAtVWRPKrRPKLFx3Jeg5CbM3xUyXR76KO1cc2Eq5OHhN9pFfhv81_YciVOqNAmYAy4AlxTNnzWGg4spQ-fy_p_fXSqXqS18Fj4xXGoDKZ0rchKzhUa5TVoQt3TaryI_3zvlbis9E_4FDXrzMMaCqKVwgTZ7r6zjDQ"
def Generate_Image(prompt):
    system(f'python -m BingImageCreator --prompt "{prompt}" -U "{u_cookie_value}"')

    return listdir("output")

Generate_Image('spiderman and batman')