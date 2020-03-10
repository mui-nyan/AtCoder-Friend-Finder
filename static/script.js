function isAuthorized() {
    return $(".authorized").val() == "true";
}

function searchFriendUsers() {
    return $.ajax({
        url: URL_FOR_FIND_FRIENDS
    });
}

function renderFriendUsers(users) {
    $(".friends_table_body").html(users.map( (user) => `
      <tr>
        <td><a href="https://atcoder.jp/users/${ user.atcoder_id }">${ user.atcoder_id }</a></td>
        <td><a href="https://twitter.com/${ user.twitter_id }">${ user.twitter_name } @${ user.twitter_id }</a></td>
      </tr>
    ` ).join(""));
}

$(function(){
    $(".find_button").on("click", e => {
        searchFriendUsers().then(data => {
            renderFriendUsers(data.data);
        });
    });
});
