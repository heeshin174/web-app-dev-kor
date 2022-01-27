import Header from "./components/Header/Header";
import List from "./components/List/List";
import Map from "./components/Map/Map";
import PlaceDetails from "./components/PlaceDetails/PlaceDetails";
import { CssBaseline, Grid } from "@material-ui/core";

function App() {
  return (
    <div className="App">
      <CssBaseline />
      <Header />
      <Grid container spacing={3} style={{ width: "100%" }}>
        <Grid item xs={12} md={4}>
          {" "}
          <List />{" "}
        </Grid>
        <Grid item xs={12} md={4}>
          {" "}
          <Map />{" "}
        </Grid>
      </Grid>
    </div>
  );
}

export default App;

// Since we are doing inline style, it has to be an object.
// So, we need double curly braces.
