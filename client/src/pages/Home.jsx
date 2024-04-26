import { useEffect, useState } from "react";
import TopBar from "../components/Navbar";
import Shop from "../components/Shop";
import Cart from "../components/Cart.jsx";
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
        <Provider store={store}>
          <Shop />
        </Provider>
      );
    } else if (tab == "Cart") {
      return (
        <Provider store={store}>
          <Cart />
        </Provider>
      );
    } else if (tab == "Settings") {
      return;
    }
  };
  return (
    <>
      <div className="h-screen flex flex-col items-center bg-gray-800 h-full">
        <TopBar updateTab={setTab} />
        <RenderTab />
      </div>
    </>
  );
}

export default Home;
