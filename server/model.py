import spacy
nlp = spacy.load("en_core_web_md")

device_types = ["phone","tablet", "smartwatch", "laptop"]
brands = ["Samsung", "Apple"]
qual_quant_types = ["RAM", "Storage", "Camera Performance"]
req_fields = {"ram":"RAM","storage":"Storage", 
            #   "camera":"Camera Performance"
              }
numeric_types = ["RAM", "Storage"]
quantifier_to_symbol = {"less": "<", "more": ">","great": ">", "atleast": ">=", "equal": "="}

def get_functionality(action: str, stk: dict, spec: dict):
    best_ans = (0, 0)
    # print("stack", stk)
    for fields in req_fields:
        doc1 = nlp(fields)
        doc2 = nlp(action)
        similarity = doc1.similarity(doc2)
        if similarity > 0.5:
            best_ans = (similarity, req_fields[fields])
            if best_ans[1] in qual_quant_types and stk:
                val = stk.pop()
                symbol = ""
                if stk != []:
                    symbol = quantifier_to_symbol[stk.pop()]
                    spec[best_ans[1] + "_" + symbol] = val
                else:
                    spec[best_ans[1] + "_="] = val
            # if best_ans[1] in numeric_types and stk:
            #     symbol = quantifier_to_symbol[stk.pop()]
            #     # spec[best_ans[1]] = symbol +  spec[best_ans[1]]
            #     spec[best_ans[1] + "_" + symbol] = spec[best_ans[1]]
            elif best_ans[1] in numeric_types and not stk:
                # spec[best_ans[1] ] =   spec[best_ans[1]]
                spec[best_ans[1] + "_="] =   spec[best_ans[1]]



def get_specs(text: str):
    
    doc = nlp(text)
    stk = []
    spec = {}
    device = ""
    brand = ""
    
    for i, token in enumerate(doc):
        # print(token.lemma_, token.pos_)
        if token.lemma_ in device_types:
            device = token.lemma_ 
        # if token.lemma_ in brands:
        #     brand = token.lemma_
        elif(token.pos_ == "NUM" or token.pos_ == "ADJ"):
            stk.append(token.lemma_)
            # print(token.pos_)
        elif (token.pos_ == "NOUN"):
            # print(i+1)
            get_functionality(token.lemma_, stk, spec)
    # print("stack",stk)
    return {"specifications": spec, "device": device}

# {
#     "specifications": {
#         "RAM": "32",
#         "Camera Performance": "nice"
#     },
#     "device": "phone"
# }

# print(get_specs("phone with greater than 1 gb ram and 1 gb storage"))
# print(get_specs("I want a phone with  23 gigs of ram and greater than 128 gigs of storage"))