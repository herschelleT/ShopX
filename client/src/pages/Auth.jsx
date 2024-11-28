import { useState } from "react";
import axios from "../api/axios";
import { useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";
import { setUserInfo, clearUserInfo } from "../store/reducers";

const SignUpLogin = () => {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isSignUp, setIsSignUp] = useState(true);
  const navigate = useNavigate();
  const handleSignUp = (e) => {
    e.preventDefault();
    // Add your sign-up logic here
    axios
      .post("/users", { email: email, password: password, type: "user" })
      .then((res) => {
        console.log("Signing up...");
        console.log(res);
        setIsSignUp(false);
      })
      .catch((err) => console.log(err));
  };

  const handleLogin = (e) => {
    e.preventDefault();
    axios
      .post(`/login`, { email: email, password: password })
      .then((res) => {
        console.log(res);
        dispatch(setUserInfo(res.data));
        navigate("/home");

        console.log("Logging in...");
      })
      .catch((err) => console.log(err));
  };

  return (
    <div className="flex justify-center items-center h-screen bg-gray-100" style={{ backgroundColor: "grey" }}>
      <div className="bg-gray-300 rounded-lg shadow-md p-8 w-96">
        <h2 className="text-3xl font-bold text-gray-800 mb-4">{isSignUp ? "Sign Up" : "Login"}</h2>
        <form onSubmit={isSignUp ? handleSignUp : handleLogin}>
          <div className="mb-4">
            <label htmlFor="email" className="block text-gray-700 font-bold mb-2">
              Email Address
            </label>
            <input
              type="email"
              id="email"
              className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-gray-600"
              placeholder="Enter your email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
          <div className="mb-6">
            <label htmlFor="password" className="block text-gray-700 font-bold mb-2">
              Password
            </label>
            <input
              type="password"
              id="password"
              className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:border-gray-600"
              placeholder="Enter your password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          <button type="submit" className="w-full bg-gray-800 text-white py-2 px-4 rounded-lg hover:bg-gray-700 focus:outline-none focus:bg-gray-700">
            {isSignUp ? "Sign Up" : "Login"}
          </button>
        </form>
        <p className="mt-4 text-gray-700">
          {isSignUp ? "Already have an account?" : "Don't have an account yet?"}{" "}
          <span className="text-gray-800 font-bold cursor-pointer" onClick={() => setIsSignUp(!isSignUp)}>
            {isSignUp ? "Login here" : "Sign up now"}
          </span>
        </p>
      </div>
    </div>
  );
};

export default SignUpLogin;
