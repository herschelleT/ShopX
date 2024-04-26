import { createStore, combineReducers } from "redux";
import itemReducer from "./reducers";

const rootReducer = combineReducers({
  items: itemReducer,
  // Add other reducers here if you have any
});

const store = createStore(rootReducer);

export default store;
