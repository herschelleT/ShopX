import React, { useEffect } from "react";
import { connect } from "react-redux";
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
import axios from "../api/axios";

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

const Cart = ({ items }) => {
  const selectedItems = items.selectedItems;
  const user = items.userInfo?.data;
  useEffect(() => {
    console.log("user", user);
  }, []);
  const handleCheckout = () => {
    selectedItems.map((ele) => {
      axios
        .post("/orders", {
          Brand: ele.Brand,
          Model: ele.Model,
          Price: ele.Price,
          user_id: user.user_id,
        })
        .then((res) => {
          console.log("order", res);
        })
        .catch((err) => {
          console.log(err);
        });
    });
  };
  return (
    <div className="cart flex flex-col align-items-center">
      <div className="flex flex-wrap justify-center mt-4 bg-gray-900" style={{ maxWidth: "1250px" }}>
        {selectedItems.map((ele, i) => (
          <div key={i}>
            <Card style={{ width: "18rem", margin: "7px", backgroundColor: "#808080" }}>
              <Card.Img variant="top" src={imagesMap[ele.Model]} style={{ width: "200px", height: "200px", objectFit: "cover" }} className="mx-auto" />

              <Card.Body>
                <Card.Title>{ele.Model}</Card.Title>
              </Card.Body>
            </Card>
          </div>
        ))}
      </div>
      <div className="" style={{}}>
        <Button
          variant="primary"
          onClick={() => {
            handleCheckout();
          }}
        >
          Proceed to Checkout
        </Button>
      </div>
    </div>
  );
};

const mapStateToProps = (state) => ({
  items: state.items,
});

export default connect(mapStateToProps)(Cart);
