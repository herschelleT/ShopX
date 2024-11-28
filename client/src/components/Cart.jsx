import React, { useEffect, useState } from "react";
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
import { useSelector } from "react-redux";

const imagesMap = {
  "iPhone 13": iPhone13, //
  "Pixel 6": pixel6,
  "P40 Pro": p40,
  "GT 5G": velvet,
  "Xperia 5 III": edge,
  "9 Pro": pro,
  "8.3 5G": x3,
  "Galaxy S21": s21, //
  "ROG Phone 5": xperia,
  "Mi 11": m11,
};

const Cart = () => {
  const [devices, setDevices] = useState();
  const userInfo = useSelector((state) => state.user.userInfo);
  const handleCheckout = () => {
    
  };
  useEffect(() => {
    axios.get(`/orders/user/${userInfo.user_id}`).then((res) => {
      console.log(res);
      setDevices(res.data)
    }).catch((err) => {
      console.error(err)
    })
  }, [])
  return (
    <div className="cart flex flex-col align-items-center h-full">
      <div className="flex flex-wrap justify-center mt-4 bg-gray-900" style={{ maxWidth: "1250px" }}>
        {devices?.map((ele, i) => (
          <div key={i}>
            <Card style={{ width: "18rem", margin: "7px", backgroundColor: "#808080" }}>
              <Card.Img variant="top" src={imagesMap[ele.model]} style={{ width: "200px", height: "200px", objectFit: "cover" }} className="mx-auto" />

              <Card.Body>
                <Card.Title>{ele.model}</Card.Title>
              </Card.Body>
            </Card>
          </div>
        ))}
      </div>
      {/* <div className="" style={{}}>
        <Button
          variant="primary"
          onClick={() => {
            handleCheckout();
          }}
        >
          Proceed to Checkout
        </Button>
      </div> */}
    </div>
  );
};


export default Cart;
