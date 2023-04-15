import QtQuick 2.15
import QtQuick.Controls 2.15
import "."

Text {
    anchors.centerIn: parent
    text: pricedata.price_data[5].toString()
    font.pixelSize: 24
}