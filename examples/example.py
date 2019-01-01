import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath("main.py"))
sys.path.append(os.path.dirname(CURRENT_DIR))
import main as m
import pandas as pd

df = pd.read_csv("testbook.csv")

fatest = m.FA_Tests()
kmo_score = fatest.KMO(df) ## Finding out the KMO score
print(kmo_score) 

c, d, k, p = fatest.BToS(df) ## Fiding out Bartlett's test values
print(c, d, k, p)

fa = m.FA()
eigenvals, eigenvectors = fa.Eigens(df)
print(eigenvals, "\n", eigenvectors) ## Getting eigen values and eigen vectors

vardf = fa.VarperComp()
print(vardf) ## Components and it's amount of explained variance and cumulative dist

# fa._PrintScreePlot() ## Scree plot

loading_df = fa.loadings()
print(loading_df)

pcs = fa.pcscores(df)
print(pcs)

varimaxrmat = fa.varimaxr(loading_df)
print(varimaxrmat)