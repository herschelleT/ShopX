import { useState, useEffect } from "react";
import axios from "../api/axios";
import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";
import testImage from "../images/test.png";
import iPhone13 from "../images/Apple_iPhone13.png";
import pixel6 from "../images/Google_Pixel6.png";
import p40 from "../images/Huawei_P40.png";
import velvet from "../images/LG_Velvet.png";
import edge from "../images/Motorola_Edge.png";
import pro from "../images/OnePlus_9Pro.png";
import x3 from "../images/Oppo_X3.png";
import s21 from "../images/Samsung_GalaxyS21.png";
import xperia from "../images/Sony_Xperia.png";
import m11 from "../images/Xiaomi_Mi11.png";
import { connect } from "react-redux";
const imagesMap = {
  "iPhone 13": iPhone13,
  "Pixel 6": pixel6,
  "P40 Pro": p40,
  Velvet: velvet,
  "Edge+": edge,
  "9 Pro": pro,
  "Find X3 Pro": x3,
  "Galaxy S21": s21,
  "Xperia 1 III": xperia,
  "Mi 11": m11,
};
const Shop = ({ selectedItems, addItem }) => {
  // console.log("Props received by Shop component:", { selectedItems, addItem });

  const [text, setText] = useState("");
  const [specs, setSpecs] = useState();
  const [fetchBtn, setFetchBtn] = useState(true);
  const [display, setDisplay] = useState([]);
  const handleSubmit = (text) => {
    axios.post("/", { body: text }).then((res) => {
      console.log(res);
      setSpecs(res.data);
    });
  };
  const handleGo = (specs) => {
    axios.post("/fetch", specs).then((res) => {
      console.log("fetch result", res);
      setDisplay(res.data.data);
    });
  };
  useEffect(() => {
    console.log("devices", display);
  }, [display]);
  // console.log("addItem prop:", addItem);

  const handleAddItem = (item) => {
    addItem(item);
  };

  const handleRemove = (modelNameToRemove) => {
    setDisplay(display.filter((ele) => ele.Model !== modelNameToRemove));
  };

  useEffect(() => {
    console.log("redux", selectedItems);
  }, []);
  return (
    <div className="">
      <div className="bg-gray-900 p-8 rounded-lg shadow-lg">
        <div className="flex items-center">
          <input
            type="text"
            className="flex-grow border border-gray-300 rounded-md py-2 px-4 mr-2 focus:outline-none focus:border-blue-500 bg-gray-800 text-white"
            placeholder="Enter text..."
            onChange={(e) => {
              setText(e.target.value);
              setFetchBtn(true);
            }}
          />
          {fetchBtn ? (
            text ? (
              <Button
                variant="primary"
                size="lg"
                className="px-6"
                onClick={() => {
                  handleSubmit(text);
                  setFetchBtn(false);
                }}
                active
              >
                Submit
              </Button>
            ) : (
              <Button variant="primary" size="lg" className="px-6" disabled>
                Submit
              </Button>
            )
          ) : (
            <Button
              variant="primary"
              className="px-6"
              size="lg"
              onClick={() => {
                handleGo(specs);
              }}
            >
              Go
            </Button>
          )}
        </div>
      </div>
      {specs && (
        <div className="max-w-2/3 bg-gray-900 p-4 rounded-lg shadow-lg mt-2">
          <div className="flex">
            {Object.entries(specs?.specifications).map(([key, value], i) => (
              <div className="bg-gray-800 p-4 rounded-lg text-white flex items-center justify-center mx-2" key={i}>
                <span className="text-xl font-semibold">
                  {key}
                  {value}
                </span>
              </div>
            ))}
          </div>
        </div>
      )}
      {display && (
        <div className="flex flex-wrap justify-center mt-4 bg-gray-900" style={{ maxWidth: "1250px" }}>
          {display.map((ele, i) => (
            // <div key={i} className="rounded flex flex-row" style={{ backgroundColor: "#7393B3", minHeight: "150px", minWidth: "150px" }}>
            //   <img src={testImage} className="max-h-20" />
            //   <div className="text-white">
            //     <p className="text-bold">{ele?.Brand}</p> {ele?.Model}
            //   </div>
            // </div>
            <div key={i}>
              <Card style={{ width: "18rem", margin: "7px", backgroundColor: "#808080" }}>
                <Card.Img
                  variant="top"
                  src={imagesMap[ele.Model]}
                  style={{
                    width: "160px",
                    height: "225px",
                    // objectFit: "cover"
                  }}
                  className="mx-auto"
                />

                <Card.Body>
                  <Card.Title>{ele.Model}</Card.Title>
                  <Button
                    variant="primary"
                    onClick={() => {
                      handleAddItem(ele);
                      handleRemove(ele.Model);
                    }}
                  >
                    Add to cart
                  </Button>
                </Card.Body>
              </Card>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
const mapStateToProps = (state) => ({
  selectedItems: state.items.selectedItems,
});

const mapDispatchToProps = (dispatch) => ({
  addItem: (item) => dispatch({ type: "ADD_ITEM", payload: item }),
});

export default connect(mapStateToProps, mapDispatchToProps)(Shop);
