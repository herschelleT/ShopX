// reducers/itemReducer.js
const initialState = {
  selectedItems: [],
  userInfo: null, // Initialize userInfo to null
};

const itemReducer = (state = initialState, action) => {
  switch (action.type) {
    case "ADD_ITEM":
      return {
        ...state,
        selectedItems: [...state.selectedItems, action.payload],
      };
    case "LOGIN":
      return {
        ...state,
        userInfo: action.payload, // Update userInfo with the user's information upon login
      };
    case "LOGOUT":
      return {
        ...state,
        userInfo: null, // Clear userInfo upon logout
      };
    default:
      return state;
  }
};

export default itemReducer;
