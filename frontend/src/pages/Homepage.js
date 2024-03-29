import { Skull } from "../components/assets/Skull";
import Login from "../components/Login";

export default function Homepage({
  auth,
  setAuth,
  setName,
  setEmail,
  setPicture
}) {

  return (
    <section className="home">
      <div className="main center">
        <div className="sub-heading">
          Team Aavishkar presents
        </div>
        <div className="heading">
          <h3>REChase 4.0</h3>
        </div>
        <Login
          auth={auth}
          {...{ setAuth }}
          {...{ setName }}
          {...{ setEmail }}
          {...{ setPicture }}
        />
      </div>
      <div className="svg-parent themed-stroke">
        <Skull />
      </div>
    </section>
  )
}
