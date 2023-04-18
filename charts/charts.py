import matplotlib.pyplot as plt

def generate_pie_chart():
    labels= ['A', 'B', 'C']
    values = [200, 34, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png') # para generar una imagen y que el proceso del codigo no se detenga, si no que genere la imagen y me la guarde
    plt.close()