import streamlit as st

# Title
st.title("EXPERIMENT1B ")
st.title("To determine the total alkalinity of water sample.")

# First concept
st.header("Prior Concept:")
st.write("Definitions of acids and bases, their types, Neutralization reaction and indicators.")

# Second concept
st.header("New Concepts:")
st.subheader("Proposition 1:")
st.write("The alkalinity of water is mainly due to the hydroxides, carbonates, bicarbonates.")

import streamlit as st
from PIL import Image

# Open an image file
img_path = "Screenshot_20231114-100609_Drive.jpg"
img = Image.open(img_path)

# Display the image using Streamlit
st.image(img,  use_column_width=True)




st.subheader("Proposition 2:")
st.write("Use of highly alkaline water in boiler may lead to caustic embrittlement and deposition of precipitates and sludge in boiler tubes and pipes.")

import streamlit as st
from PIL import Image

# Open an image file
img_path = "Screenshot_20231114-100629_Drive.jpg"
img = Image.open(img_path)

# Display the image using Streamlit
st.image(img,  use_column_width=True)



st.subheader("Proposition 3:")
st.write("Hence, it is essential to have an idea about the nature and extent of alkalinity. This can be determined by performing neutralization titration between alkaline water sample Vs standard acid solution. From the amount of std. acid used exact amount and nature of alkalinity is found out.")

import streamlit as st
from PIL import Image

# Open an image file
img_path = "Screenshot_20231114-100653_Drive.jpg"
img = Image.open(img_path)

# Display the image using Streamlit
st.image(img,  use_column_width=True)



st.header("Information Input:")
st.write("i) The neutralization titration is performed using N/50 acid and it has two end points. First one corresponds to Phenolphthalein end point and second one to methyl orange end point (M).")
st.write("ii) To obtain first end point, phenolphthalein is used as indicator and for use of methyl orange is done for yielding second end point.")
st.write("iii) Volume of acid required for getting Phenolphthalein end point is V1 and for obtaining methyl orange end point V2.")
st.write("iv) Types of alkalinities present in the water sample.")

import streamlit as st
from PIL import Image

# Open an image file
img_path = "Screenshot_20231114-100716_Drive.jpg"
img = Image.open(img_path)

# Display the image using Streamlit
st.image(img,  use_column_width=True)

st.header("Apparatus: -")
st.write("burette, pipette, conical flask, 100ml measuring cylinder, etc.")

st.header("Chemicals: -")
st.write("Water sample, phenolphthalein, N/50 HCl, methyl orange.")

st.header("Stepwise Procedure:-")
st.write("Take 100ml of water sample to be tested in a titration flask. To it add 2 to 3 drops of phenolphthalein and titrate the sample against standard N/50 HCl until the phenolphthalein end point [P].")
st.write("To this above same solution add 2 to 3 drops of methyl orange; continue the titration until the sharp color changes from yellow to red. Note the total reading as methyl orange end point [M].")


st.header("Observations:-")
st.subheader("[I] For phenolphthalein end point. [P]")
st.write("1) In Burette ---- N/50 HCl solutions")
st.write("2) In Conical flask ---- 100ml water sample.")
st.write("3) Indicator ------ Phenolphthalein")
st.write("4) End Point ----- Pink to Colorless")
st.subheader("[II] For methyl orange end point. [M]")
st.write("1) In Burette ---- N/50 HCl solution")
st.write("2) In Conical flask ----same solution from phenolphthalein end point.")
st.write("3) Indicator ------ Bromocresol")
st.write("4) End Point ----- Blue to green")

st.subheader("Observation Table I –:")
import streamlit as st

def main():
    st.header("Volume of N/50 HCl required")

    # Get user input for the number of samples
    num_samples = st.number_input("Enter the number of samples:", min_value=1, step=1)

    # Create a table
    table = [["Sample No.", "Phenolphthalein endpoint [P] (V1 ml)", "Methyl Orange endpoint [M] (V2 ml)"]]

    # Populate the table with user input
    for i in range(1, num_samples + 1):
        sample_no = i
        p_endpoint = st.number_input(f"{i}. Phenolphthalein endpoint [P] (V1 ml):", min_value=0.0, step=0.1)
        m_endpoint = st.number_input(f"{i}. Methyl Orange endpoint [M] (V2 ml):", min_value=0.0, step=0.1)

        # Add a row to the table
        table.append([sample_no, p_endpoint, m_endpoint])

    # Display the table
    st.table(table)

if __name__ == "__main__":
    main()


st.header("Calculations:-")
st.write("Alkalinity is expressed as parts per million in terms of CaCO3")
st.write("As 1000ml of 1N HCl= 50 gm of CaCO3")
st.write("Determine alkalinity in water sample in mg/lit (ppm) for Phenolphthalein alkalinity P (considering V1) in ppm Methyl orange alkalinity M (considering V2) in ppm")
st.write("1) For water sample having only hydroxide alkalinity, it gets neutralized at Phenolphthalein end point i.e. when V1 ml acid is added. Here V2 will be zero.")

import streamlit as st

def main():
    st.write("Phenolphthalein Endpoint Calculation")

    # Get user input for volume
    V1 = st.number_input("Enter the volume (ml):", min_value=0.0, step=0.1)

    # Display entered volume
    st.write(f"Phenolphthalein endpoint V1 = {V1} ml")

if __name__ == "__main__":
    main()

import streamlit as st

def main():
    st.write("Alkalinity Calculation")

    # Get user input for P
    P = st.number_input("Enter the value of P (ppm):", min_value=0.0, step=0.1)

    # Display entered value of P
    st.write(f"Alkalinity due to OH- = {P} ppm")

if __name__ == "__main__":
    main()


st.write("2) For water sample having V1=0, water contains only bicarbonate alkalinity.")

import streamlit as st

def main():
    st.write("Methyl Orange Endpoint Calculation")

    # Get user input for V2
    V2 = st.number_input("Enter the volume (ml) for Methyl Orange endpoint:", min_value=0.0, step=0.1)

    # Display entered volume
    st.write(f"Methyl Orange endpoint V2 = {V2} ml")

if __name__ == "__main__":
    main()

import streamlit as st

def main():
    st.write("Alkalinity Calculation")

    # Get user input for M
    M = st.number_input("Enter the value of M (ppm):", min_value=0.0, step=0.1)

    # Display entered value of (2P-M)
    st.write(f"Alkalinity due to HCO3- = {M} ppm")

if __name__ == "__main__":
    main()


st.write("3) If water sample contains hydroxide and carbonate alkalinity, then Phenolphthalein end point corresponds to slightly higher than half neutralization of carbonate i.e V1 >1/2 V2")



import streamlit as st

def main():
    st.write("Alkalinity Calculation")

    # Get user input for (2P-M)
    X = st.number_input("Enter the value of (2P-M) (ppm):", min_value=0.0, step=0.1)

    # Display entered value of (2P-M)
    st.write(f"Alkalinity due to OH- = {X} ppm")

if __name__ == "__main__":
    main()


import streamlit as st

def main():
    st.write("Alkalinity Calculation")

    # Get user input for 2(M-P)
    Y = st.number_input("Enter the value of 2(M-P) (ppm):", min_value=0.0, step=0.1)

    # Display entered value of 2(M-P)
    st.write(f"Alkalinity due to CO3^2- = {Y} ppm")

if __name__ == "__main__":
    main()


import streamlit as st

def main():
    st.header("RESULTS:")

    # Get user input for the number of water samples
    num_samples = st.number_input("Enter the number of water samples:", min_value=1, step=1)

    # Create a table
    table = [["Water Sample", "OH- Alkalinity (ppm)", "CO3 Alkalinity (ppm)", "HCO3 Alkalinity (ppm)"]]

    # Populate the table with user input
    for i in range(1, num_samples + 1):
        water_sample = st.text_input(f"{i}. Water Sample:")
        oh_alkalinity = st.number_input(f"{i}. OH- Alkalinity (ppm):", min_value=0, step=1)
        co3_alkalinity = st.number_input(f"{i}. CO3 Alkalinity (ppm):", min_value=0, step=1)
        hco3_alkalinity = st.number_input(f"{i}. HCO3 Alkalinity (ppm):", min_value=0, step=1)

        # Add a row to the table
        table.append([water_sample, oh_alkalinity, co3_alkalinity, hco3_alkalinity])

    # Display the table
    st.table(table)

if __name__ == "__main__":
    main()