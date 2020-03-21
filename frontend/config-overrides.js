const {override, addWebpackAlias} = require('customize-cra');
const path = require('path');

const {
    REACT_APP_BUNDLE_TYPE = 'local',
    REACT_APP_RUTOKEN_CERT_ID,
} = process.env;

const alias = {
    mocks: path.resolve('./src/__mocks__/'),
    __mocks__: path.resolve('./src/__mocks__/'),
    '@markoffice/api': path.resolve('./api/index.js'),
    '@markoffice/data-provider': REACT_APP_BUNDLE_TYPE === 'demo'
        ? path.resolve('./src/api/provider.demo.js')
        : path.resolve('./src/api/provider.api.js'),
    '@markoffice/rutoken': REACT_APP_RUTOKEN_CERT_ID //eslint-disable-line
        ? path.resolve('./src/utils/rutoken/fouras.js')
        : (
            REACT_APP_BUNDLE_TYPE === 'local'
                ? path.resolve('./src/utils/rutoken/rutoken.local.js')
                : path.resolve('./src/utils/rutoken/rutoken.cloud.js')
        ),
};

module.exports = override(addWebpackAlias(alias));

module.exports.alias = alias;
