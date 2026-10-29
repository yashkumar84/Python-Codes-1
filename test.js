import http from "k6/http";

export const options = {
  vus: 10000,
  duration: "1h",
};

export default function () {
  const response = http.get("https://schoolites.com/");

  console.log(`Status: ${response.status}`);
}
