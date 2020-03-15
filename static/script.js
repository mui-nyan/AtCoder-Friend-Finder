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
        <td><a target=”_blank” href="https://atcoder.jp/users/${ user.atcoder_id }">${ user.atcoder_id }</a></td>
        <td><a target=”_blank” href="https://twitter.com/${ user.twitter_id }">${ user.twitter_name } @${ user.twitter_id }</a></td>
        <td>${ user.rating }</td>
        <td><img src="${ user.profile_img }"></td>
      </tr>
    ` ).join(""));
}

function tweetButton(num) {
    $(".tweet_button_wrapper").html(`<a href="https://twitter.com/intent/tweet" class="twitter-share-button" data-text="私はAtCoderユーザのTwitterを${num}人フォローしています。" data-url="https://atcoder-friend-finder.herokuapp.com/" data-lang="ja">Tweet</a>`);
    twttr.widgets.load();
}

$(function(){
    $(".find_button").on("click", e => {
        $(".find_button").prop("disabled", true);
        $(".friends_table_body").html("");
        $(".friends_table_body").addClass("loading");

        searchFriendUsers().then(data => {
            renderFriendUsers(data.data);
            tweetButton(data.size);
        }).always(() => {
            $(".friends_table_body").removeClass("loading");
            $(".find_button").prop("disabled", false);
        });
    });
});
