### **Sentence Segmentation**

Determination of boundaries between sentences





### **Tokenisation**

**Challenges**

- ASCII only?
- Unicode(UTF-8)



**To split or not to split**

- Sentence segementation (split)
- Tokenisation (split)
- Named entity recognition (combine)

tokenisation is **knowing when to split** (not when to combine)



### Annotation Formats

undertanding documents: Documents are meant to be human-readable.

how to make the machine understand the documents?



Annotations: Enabling machine-readability



**Boundary Notation**

BIO: B=Begin, I=Inside, O=Outside



**Stand-off annotations**

annotations are stored separately.

requires **a way to link between annotations and text**.

links annotations to text using indexing based on **character offsets**.



**Strengths**

- original raw text is left untouched
- can handle structured and overlapping annotations



**Limitations**

- not readily human-readable



### Distributional Semantics

#### 