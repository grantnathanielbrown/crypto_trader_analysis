const axios = require('axios');
const util = require('util');

const api_key = process.env.DEFINED_API_KEY;

axios
  .post(
    "https://graph.defined.fi/graphql",
    {
      query: `
        query {
          getTokenPrices(
            inputs: [
              {
                address: "0x5c8627faa7178fec478eb1ae789d472704c08edb",
                networkId: 1,
                timestamp: 1698715463
              },
              {
                address: "0x5c8627faa7178fec478eb1ae789d472704c08edb",
                networkId: 1,
                timestamp: 1698715493
              },
              {
                address: "0x5c8627faa7178fec478eb1ae789d472704c08edb",
                networkId: 1,
                timestamp: 1698715763
              },
              {
                address: "0x5c8627faa7178fec478eb1ae789d472704c08edb",
                networkId: 1,
                timestamp: 1698716363
              },
              {
                address: "0x5c8627faa7178fec478eb1ae789d472704c08edb",
                networkId: 1,
                timestamp: 1698719093
              },
              {
                address: "0x5c8627faa7178fec478eb1ae789d472704c08edb",
                networkId: 1,
                timestamp: 1698729863
              },
              {
                address: "0x5c8627faa7178fec478eb1ae789d472704c08edb",
                networkId: 1,
                timestamp: 1698801863
              },
              {
                address: "0x5c8627faa7178fec478eb1ae789d472704c08edb",
                networkId: 1,
                timestamp: 1699320293
              },
              {
                address: "0x5c8627faa7178fec478eb1ae789d472704c08edb",
                networkId: 1,
                timestamp: 1701307493
              },
             
            ]
          ) {
            address
            networkId
            priceUsd
          }
        }
      `
    },
    {
      headers: {
        "Content-Type": "application/json",
        "Authorization": api_key
      }
    }
  )
  .then((response) => {
    console.log(util.inspect(response.data, { showHidden: false, depth: 3, colors: true }));
  });
