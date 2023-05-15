from fpdf import FPDF


def main():

    name = input("Name: ")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 50)
    pdf.text(35, 40, "CS50 Shirtificate")

    pdf.image("shirtificate.png", w=pdf.epw, x=10, y=70)
    pdf.set_font_size(30)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 250, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")



if __name__ == "__main__":
    main()