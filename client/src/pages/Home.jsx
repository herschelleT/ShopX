import { useEffect, useState } from "react";
import TopBar from "../components/Navbar";
import Shop from "../components/Shop";
import Cart from "../components/Cart.jsx";
import Dashboard from "../components/Dashboard.jsx";
import { Provider } from "react-redux";
import store from "../store/index.js";

function Home() {
  const [tab, setTab] = useState("Shop");
  useEffect(() => {
    console.log("tab", tab);
  }, [tab]);
  const RenderTab = () => {
    if (tab == "Shop") {
      return (
          <Shop updateTab={setTab}/>
      );
    } else if (tab == "Wishlist") {
      return (
          <Cart />
      );
    } else if (tab == "Settings") {
      return;
    } else if (tab == "Admin") {
      return (
        <Dashboard />
      )
    }
  };
  return (
    <>
      <div className="flex flex-col items-center bg-gray-800 min-h-screen">
        <TopBar updateTab={setTab} />
        <RenderTab />
      </div>
    </>
  );
}

export default Home;
