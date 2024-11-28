import { useState, useEffect } from "react";
import axios from "../api/axios";

import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";
import Badge from "react-bootstrap/Badge";

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

import Slider from 'rc-slider';
import 'rc-slider/assets/index.css';
import 'bootstrap/dist/css/bootstrap.min.css';

import ReviewModal from "../components/ReviewsModal"
import { Modal } from "react-bootstrap";
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
const labelStyle = { color: '#f1f1f1' }; 
const Shop = () => {
  const [priceRange, setPriceRange] = useState([0, 1000]);
  const [ramRange, setRamRange] = useState([2, 16]);
  const [storageRange, setStorageRange] = useState([32, 512]);
  const [batteryRange, setBatteryRange] = useState([2000, 6000]);
  const [screenSizeRange, setScreenSizeRange] = useState([4.5, 7.0]);

  const handlePriceChange = (value) => setPriceRange(value);
  const handleRamChange = (value) => setRamRange(value);
  const handleStorageChange = (value) => setStorageRange(value);
  const handleBatteryChange = (value) => setBatteryRange(value);
  const handleScreenSizeChange = (value) => setScreenSizeRange(value);

  const [selectedCards, setSelectedCards] = useState([]);
  const [showModal, setShowModal] = useState(false);

  const [isModalOpen, setIsModalOpen] = useState(false);
  const [currId, setCurrId] = useState();

  const openModal = () => setIsModalOpen(true);
  const closeModal = () => setIsModalOpen(false);

  const [cheapestIdx, setCheapestIdx] = useState(-1);
  const [highestRatingIdx, setHighestRatingIdx] = useState(-1);
  const [mostLikedIdx, setMostLinkedIdx] = useState(-1);

  const applyFilters = async () => {
    try {
      const response = await axios.post('/phones/search', {
        min_ram: ramRange[0] || null,
        max_ram: ramRange[1] || null,
        min_storage: storageRange[0] || null,
        max_storage: storageRange[1] || null,
        // min_camera: filters.min_camera || null,
        // max_camera: filters.max_camera || null,
        min_screen_size: screenSizeRange[0] || null,
        max_screen_size: screenSizeRange[1] || null,
        min_battery_capacity: batteryRange[0] || null,
        max_battery_capacity: batteryRange[1] || null,
        // battery_rating: filters.battery_rating || null,
        min_price: priceRange[0] || null,
        max_price: priceRange[1] || null,
      });
  
      console.log(response.data)
//       cheapest_phone_index
// : 
// 8
// most_ordered_phone_index
// : 
// 1
// most_rated_phone_index
// : 
0
      setCheapestIdx(response.data.cheapest_phone_id)
      setHighestRatingIdx(response.data.most_rated_phone_id)
      setMostLinkedIdx(response.data.most_ordered_phone_id)
      setDisplay(response.data.phones)
      // return response.data;  // Return the list of phones matching the criteria
    } catch (error) {
      console.error("Error fetching phones:", error);
      throw error;
    }
  };
  const [text, setText] = useState("");
  const [specs, setSpecs] = useState();
  const [fetchBtn, setFetchBtn] = useState(true);
  const [display, setDisplay] = useState([]);

  const userInfo = useSelector((state) => state.user.userInfo);
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

  const handleAddItem = async (item) => {
    try {
      console.log("item", item);
      
      const payload = {Brand: item.brand, Model: item.model, user_id: userInfo.user_id, phone_id: item.id}
      console.log(payload);
      const response = await axios.post('/orders/', payload);
    } catch (error) {
      console.error(error);
    }
  };

  const handleRemove = (modelNameToRemove) => {
    setDisplay(display.filter((ele) => ele.Model !== modelNameToRemove));
  };

  const handleCardSelect = (ele) => {
    if (selectedCards.length < 2) {
      setSelectedCards([...selectedCards, ele]);
    } else {
      setSelectedCards([ele]); // Reset if more than 2 are selected
    }
  };

  const handleShowModal = () => {
    if (selectedCards.length === 2) setShowModal(true);
  };

  const handleCloseModal = () => {
    setShowModal(false);
    setSelectedCards([]); // Reset selection after closing modal
  };

  useEffect(() => {
    const handleShowModal = () => {
      if (selectedCards.length === 2) setShowModal(true);
    };
    handleShowModal();
  }, [selectedCards])
  return (
    <div className="w-full">
      <div className="container w-240 border mt-4 p-4 rounded text-light w-2/5" style={{"backgroundColor": "#2c3e50"}}>
            {/* Price Range */}
            <div className="filter-group mb-3">
                <label style={labelStyle}>Price Range ($): {priceRange[0]} - {priceRange[1]}</label>
                <Slider
                    min={0}
                    max={2000}
                    defaultValue={priceRange}
                    onChange={handlePriceChange}
                    range
                    allowCross
                />
            </div>

            {/* RAM Slider */}
            <div className="filter-group mb-3">
                <label style={labelStyle}>RAM (GB): {ramRange[0]} - {ramRange[1]}</label>
                <Slider
                    min={2}
                    max={32}
                    defaultValue={ramRange}
                    onChange={handleRamChange}
                    range
                    allowCross
                />
            </div>

            {/* Storage Slider */}
            <div className="filter-group mb-3">
                <label style={labelStyle}>Storage (GB): {storageRange[0]} - {storageRange[1]}</label>
                <Slider
                    min={32}
                    max={512}
                    defaultValue={storageRange}
                    onChange={handleStorageChange}
                    range
                    allowCross
                />
            </div>

            {/* Battery Slider */}
            <div className="filter-group mb-3">
                <label style={labelStyle}>Battery (mAh): {batteryRange[0]} - {batteryRange[1]}</label>
                <Slider
                    min={2000}
                    max={6000}
                    defaultValue={batteryRange}
                    onChange={handleBatteryChange}
                    range
                    allowCross
                />
            </div>

            {/* Screen Size Slider */}
            <div className="filter-group mb-3">
                <label style={labelStyle}>Screen Size (inches): {screenSizeRange[0]} - {screenSizeRange[1]}</label>
                <Slider
                    min={4.5}
                    max={7.0}
                    step={0.1}
                    defaultValue={screenSizeRange}
                    onChange={handleScreenSizeChange}
                    range
                    allowCross
                />
            </div>

            <button className="btn btn-primary" onClick={applyFilters}>Apply Filters</button>
      </div>
      <div className="container bg-gray-900 p-8 rounded-lg shadow-lg w-2/5">

        {/* <div className="flex items-center">
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
        </div> */}
      </div>
      {/* {specs && (
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
      )} */}
      {display && (
        <div className="container flex flex-wrap justify-center mt-4 bg-gray-900" style={{ maxWidth: "1250px" }}>
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
                  src={imagesMap[ele.model]}
                  style={{
                    width: "160px",
                    height: "225px",
                    // objectFit: "cover"
                  }}
                  className="mx-auto"
                />

                <Card.Body>
                  <Card.Title>{ele.model}</Card.Title>
                  {cheapestIdx==ele.id && (
                    <Badge bg="success" className="me-1">
                      Cheapest
                    </Badge>
                  )}
                  {mostLikedIdx==ele.id && (
                    <Badge bg="danger" className="me-1">
                      Most Liked
                    </Badge>
                  )}
                  {highestRatingIdx==ele.id && (
                    <Badge bg="primary" className="me-1">
                      Most Ordered
                    </Badge>
                  )}
                  <Button
                    variant="primary"
                    onClick={() => {setCurrId(ele.id); openModal();}}
                  >
                    Check reviews
                  </Button>
                  <Button
                    variant="primary"
                    onClick={() => {
                      handleCardSelect(ele);
                      handleShowModal();
                    }}
                  > 
                    Select
                  </Button>
                  <Button
                    variant="primary"
                    onClick={() => handleAddItem(ele)}
                  > 
                    Add to wishlist
                  </Button>
                </Card.Body>
              </Card>
            </div>
          ))}
        </div>
      )}
      <div>
      {/* <button onClick={openModal}>Open Modal</button> */}

      <ReviewModal isOpen={isModalOpen} onClose={closeModal} id={currId} />
    
      {/* Modal for Side-by-Side Comparison */}
      <Modal show={showModal} onHide={handleCloseModal}>
        <Modal.Header closeButton>
          <Modal.Title>Compare Stats</Modal.Title>
        </Modal.Header>
        <Modal.Body className="d-flex justify-content-around">
          {selectedCards.map((card, index) => (
            <div key={index} className="text-center">
              <h5>{card.model}</h5>
              <p>Brand: {card.brand}</p>
              <p>RAM: {card.ram}GB</p>
              <p>Storage: {card.storage}GB</p>
              <p>Screen: {card.screen_size} in.</p>
              <p>Battery Capacity: {card.battery_capacity}mAh</p>
              <p>Price: ₹{card.price}</p>

              {/* Add more stats as needed */}
            </div>
          ))}
        </Modal.Body>
      </Modal>
    </div>
    </div>
  );
};

export default Shop;
