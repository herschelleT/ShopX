import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Auth from "./pages/Auth";
import Home from "./pages/Home";
import { Provider } from "react-redux";
import store from "./store";

export default function App() {
  return (
    <Router>
      <Routes>
        <Route
          path="/auth"
          element={
            <Provider store={store}>
              <Auth />
            </Provider>
          }
        />
        <Route path="/home" element={<Home />} />
      </Routes>
    </Router>
  );
}
